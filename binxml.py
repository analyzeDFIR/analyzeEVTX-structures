## -*- coding: UTF-8 -*-
## binxml.py
##
## Copyright (c) 2018 analyzeDFIR
## 
## Permission is hereby granted, free of charge, to any person obtaining a copy
## of this software and associated documentation files (the "Software"), to deal
## in the Software without restriction, including without limitation the rights
## to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
## copies of the Software, and to permit persons to whom the Software is
## furnished to do so, subject to the following conditions:
## 
## The above copyright notice and this permission notice shall be included in all
## copies or substantial portions of the Software.
## 
## THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
## IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
## FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
## AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
## LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
## OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
## SOFTWARE.
try:
    from shared_structures.windows.guid import *
except ImportError:
    from .shared_structures.windows.guid import *

BinXMLName = Struct(
    Padding(4),
    'NameHash'              / Int16ul,
    'NameSize'              / Int16ul,
    'Name'                  / CString('utf16')
)
BinXMLElementStart = Struct(
    'DependencyIdentifier'  / Int16ul,
    'DataSize'              / Int32ul,
    'DataOffset'            / Int32ul
)
BinXMLFragmentHeader = Struct(
    'MajorVersion'          / Int8ul, 
    'MinorVersion'          / Int8ul, 
    'Flags'                 / Int8ul
)
BinXMLTemplateDefinitionHeader = Struct(
    Padding(5),
    'DataOffset'            / Int32ul,
    Padding(4),
    'TemplateIdentifier'    / NTFSGUID,
    'DataSize'              / Int32ul
)

"""
def ValueTypeDispatcher(token):
    '''
    Args:
        token: ByteString   => token to map
    Returns:
        Function<Any> -> Any
        Function to parse value type
    Preconditions:
        token is of type ByteString
    '''
    assert isinstance(token, bytes)
    try:
        token = Int8ul.parse(token)
    except Exception as e:
        raise ValueError('unable to parse token %s as 8-bit integer'%token)
    if token == 0x00:
        return str()
    elif token == 0x01:
        return 

def NodeDispatcher(token):
    '''
    Args:
        token: ByteString   => token to map
    Returns:
        BinXMLNode
        Class for mapping binary XML token types to
        corresponding parser
    Preconditions:
        token is of type ByteString
    '''
    assert isinstance(token, bytes)
    try:
        token = Int8ul.parse(token)
    except Exception as e:
        raise ValueError('unable to parse token %s as 8-bit integer'%token)
    if token == 0x0F:
        return BinXMLFragmentHeader
    elif token == 0x01 or token == 0x41:
        return BinXMLElementStart
    elif token == 0x02:
        return BinXMLElementStartClose
    elif token == 0x03:
        return BinXMLEmptyElementClose
    elif token == 0x04:
        return BinXMLElementEnd
    elif token == 0x05 or token == 0x45:
        return BinXMLValue
    elif token == 0x06 or token == 0x46:
        return BinXMLAttribute
    elif token == 0x07 or token == 0x47:
        return BinXMLCDATASection
    elif token == 0x08 or token == 0x48:
        return BinXMLCharRef
    elif token == 0x09 or token == 0x49:
        return BinXMLEntityRef
    elif token == 0x0A:
        return BinXMLPITarget
    elif token == 0x0B:
        return BinXMLPIData
    elif token == 0x0C:
        return BinXMLTemplateInstance
    elif token == 0x0D:
        return  BinXMLNormalSubstitution
    elif token == 0x0E:
        return BinXMLNormalSubstitution
    else:
        raise ValueError('unknown token %s encountered'%token)
----
BinXML Elemen Start
    + Token type: 0x01 | 0x41
    + Dependency identifier
    + Data size
    + Attribute List
BinXML Attribute List
    + Data size
    + Bin XML Attribute array
BinXML Attribute
    + Token type: 0x06 | 0x46
    + Attribute name offset (Bin XML Name)
    + Attribute data
        + Value text
        + Substitution
        + Character reference
        + Entity reference
BinXML Attribute Name
    + Unknown
    + Name hash
    + Number of characters
    + Name string
BinXML Value Text
    + Token type: 0x05 | 0x45
    + Value type
        + 0x01: StringType
    +Value data
BinXML Substitution
    + Normal Substitution
        + Token type: 0x0D
        + Substitution Identifier
        + Value type
    + Optional Substitution
        + Token type: 0x0E
        + Substitution Identifier
        + Value type
BinXML Character Reference
    + Token type: 0x08 | 0x48
    + Character value
BinXML Entity Reference
    + Token type: 0x09
    + Entity name offset
BinXML CDATA
    + Token type: 0x07 | 0x47
    + BinXML Text String
BinXML Text String
    + Number of characters
    + String
BinXML Template Instance
    + Token type: 0x0C
    + Template definition
    + Template instance data
BinXML Template Definition
    + Unknown
    + Template data offset
    + Unknown
    + GUID
    + Template data size
    + BinXML Fragment Header
    + BinXML Element
    + Token type: 0x00
BinXML Template Instance
    + Template value count
    + Template value descripter array
    + Template value data array
BinXML Template Value Descriptor
    + Value size
    + Value type
    + Unknown
BinXML PI Target
    + Token type: 0x0A
    + PI target name offset
BinXML PI Data
    + Token type: 0x0B
    + BinXML Text String
BinXML Value Type:
        + 0x00: NullType
        + 0x01: StringType
        + 0x02: AnsiStringType
        + 0x03: Int8Type
        + 0x04: UInt8Type
        + 0x05: Int16Type
        + 0x06: UInt16Type
        + 0x07: Int32Type
        + 0x08: UInt32Type
        + 0x09: Int64Type
        + 0x0a: UInt64Type
        + 0x0b: Real32Type
        + 0x0c: Real64Type
        + 0x0d: BoolType
        + 0x0e: BinaryType
        + 0x0f: GuidType
        + 0x10: SizeTType
        + 0x11: FileTimeType
        + 0x12: SysTimeType
        + 0x13: SidType
        + 0x14: HexInt32Type
        + 0x15: HexInt64Type
"""
