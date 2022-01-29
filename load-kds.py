import boto3
import base64
import sys
import json

usage = "python load-kds.py <Kinesis Data Stream Name>"
kds_stream = sys.argv[1]

s3_bucket = "d2e-demos-published"
s3_key_prefix = "cs-immersion-day/"
s3_src_data = "labs/twitter.json"

# Make KDS client
kds = boto3.client('kinesis')

# Open S3 file
s3 = boto3.resource('s3')
objs = s3.Object(s3_bucket, s3_key_prefix + s3_src_data).get()['Body'].read().decode('utf-8').splitlines()

# For each line in S3 file, insert record into KDS
print(f"Loading records into {kds_stream}...", file=sys.stderr)
ct = 0
batch_size = 10
batch = []
first_seq = None
for obj in objs:
    record = json.loads(obj)
    ct = ct + 1
    batch.append({"PartitionKey": "pkey", "Data": (json.dumps(record)+"\n").encode('utf-8')})
    if (len(batch) > batch_size):
        res = kds.put_records(StreamName=kds_stream, Records=batch)
        if first_seq is None:
            first_seq = res["Records"][0]["SequenceNumber"]
        batch.clear()

if (len(batch) > 0):
    res = kds.put_records(StreamName=kds_stream, Records=batch)
    if first_seq is None:
        first_seq = res["Records"][0]["SequenceNumber"]
    batch.clear()

print(f"Loaded {ct} records", file=sys.stderr)
shard_iterator = kds.get_shard_iterator(StreamName=kds_stream, ShardId='shardId-000000000000', ShardIteratorType='AT_SEQUENCE_NUMBER', StartingSequenceNumber=first_seq)
print(f"Shard iterator for the start of the records in the stream:", file=sys.stderr)
print(f"{shard_iterator['ShardIterator']}")
