# Test whether the logic is correct after refactoring
from blackboxprotobuf import ProtobufFactory
if __name__ == "__main__":
    data = {"1": "aaa", "2": b'bbbbbbb'}
    typedef = {
        "1": {"type": "string"},
        "2": {"type": "bytes"}
    }
    data = ProtobufFactory.protobuf_encode(data, typedef)
    print(data)

    decode_data, decode_typedef = ProtobufFactory.protobuf_decode(data)
    print(decode_data)
    print(decode_typedef)