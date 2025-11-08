# BlackBox Protobuf Library

## Description
This project is a restructured and extended version of [blackboxprotobuf](https://github.com/nccgroup/blackboxprotobuf) by Ryan Winkelmaier.

- Retained only the two most useful APIs
- Added higher-level wrappers
- Improved code structure for maintainability

Blackbox protobuf library is a Python module for decoding and re-encoding protobuf
messages without access to the source protobuf descriptor file. This library
provides a simple Python interface to encode/decode messages that can be
integrated into other tools.

This library is targeted towards use in penetration testing where being able to
modify messages is critical and a protocol buffer definition may not be readily
available.

## Background
Protocol Buffers (protobufs)  are a standard published by Google with
accompanying libraries for binary serialization of data. Protocol buffers are
defined by a `.proto` file known to both the sender and the receiver. The actual
binary message does not contain information such as field names or most type
information.

For each field, the serialized protocol buffer includes two pieces of metadata,
a field number and the wire type. The wire type tells a parser how to parse the
length of the field, so that it can be skipped if it is not known (one protocol
buffer design goal is being able to handle messages with unknown fields). A
single wire-type generally encompasses multiple protocol buffer types, for
example the length delimited wire-type can be used for string, bytestring,
inner message or packed repeated fields. See
<https://developers.google.com/protocol-buffers/docs/encoding#structure> for
the breakdown of wire types.

The protocol buffer compiler (`protoc`) does support a similar method of
decoding protocol buffers without the definition with the `--decode_raw`
option. However, it does not provide any functionality to re-encode the decoded
message.

## How it works
The library makes a best effort guess of the type based on the provided wire type (and
occasionally field content) and builds a type definition that can be used to
re-encode the data. In general, most fields of interest are likely to be parsed
into a usable form. Users can optionally pass in custom type definitions that
override the guessed type. Custom type definitions also allow naming of fields to
improve user friendliness.

# Usage
All APIs are encapsulated in the `ProtobufFactory` class.

Example usage can be found in the test directory:  
[tests/](https://github.com/aFunnyStrange/blackboxprotobuf/tree/main/tests)