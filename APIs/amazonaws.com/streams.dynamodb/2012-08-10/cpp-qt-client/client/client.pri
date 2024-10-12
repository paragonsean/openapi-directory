QT += network

HEADERS += \
# Models
    $${PWD}/OAIAttributeValue.h \
    $${PWD}/OAIDescribeStreamInput.h \
    $${PWD}/OAIDescribeStreamOutput.h \
    $${PWD}/OAIDescribeStreamOutput_StreamDescription.h \
    $${PWD}/OAIGetRecordsInput.h \
    $${PWD}/OAIGetRecordsOutput.h \
    $${PWD}/OAIGetShardIteratorInput.h \
    $${PWD}/OAIGetShardIteratorOutput.h \
    $${PWD}/OAIIdentity.h \
    $${PWD}/OAIKeySchemaElement.h \
    $${PWD}/OAIKeyType.h \
    $${PWD}/OAIListStreamsInput.h \
    $${PWD}/OAIListStreamsOutput.h \
    $${PWD}/OAIOperationType.h \
    $${PWD}/OAIRecord.h \
    $${PWD}/OAIRecord_dynamodb.h \
    $${PWD}/OAIRecord_userIdentity.h \
    $${PWD}/OAISequenceNumberRange.h \
    $${PWD}/OAIShard.h \
    $${PWD}/OAIShardIteratorType.h \
    $${PWD}/OAIShard_SequenceNumberRange.h \
    $${PWD}/OAIStream.h \
    $${PWD}/OAIStreamDescription.h \
    $${PWD}/OAIStreamRecord.h \
    $${PWD}/OAIStreamStatus.h \
    $${PWD}/OAIStreamViewType.h \
# APIs
    $${PWD}/OAIDefaultApi.h \
# Others
    $${PWD}/OAIHelpers.h \
    $${PWD}/OAIHttpRequest.h \
    $${PWD}/OAIObject.h \
    $${PWD}/OAIEnum.h \
    $${PWD}/OAIHttpFileElement.h \
    $${PWD}/OAIServerConfiguration.h \
    $${PWD}/OAIServerVariable.h \
    $${PWD}/OAIOauth.h

SOURCES += \
# Models
    $${PWD}/OAIAttributeValue.cpp \
    $${PWD}/OAIDescribeStreamInput.cpp \
    $${PWD}/OAIDescribeStreamOutput.cpp \
    $${PWD}/OAIDescribeStreamOutput_StreamDescription.cpp \
    $${PWD}/OAIGetRecordsInput.cpp \
    $${PWD}/OAIGetRecordsOutput.cpp \
    $${PWD}/OAIGetShardIteratorInput.cpp \
    $${PWD}/OAIGetShardIteratorOutput.cpp \
    $${PWD}/OAIIdentity.cpp \
    $${PWD}/OAIKeySchemaElement.cpp \
    $${PWD}/OAIKeyType.cpp \
    $${PWD}/OAIListStreamsInput.cpp \
    $${PWD}/OAIListStreamsOutput.cpp \
    $${PWD}/OAIOperationType.cpp \
    $${PWD}/OAIRecord.cpp \
    $${PWD}/OAIRecord_dynamodb.cpp \
    $${PWD}/OAIRecord_userIdentity.cpp \
    $${PWD}/OAISequenceNumberRange.cpp \
    $${PWD}/OAIShard.cpp \
    $${PWD}/OAIShardIteratorType.cpp \
    $${PWD}/OAIShard_SequenceNumberRange.cpp \
    $${PWD}/OAIStream.cpp \
    $${PWD}/OAIStreamDescription.cpp \
    $${PWD}/OAIStreamRecord.cpp \
    $${PWD}/OAIStreamStatus.cpp \
    $${PWD}/OAIStreamViewType.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
