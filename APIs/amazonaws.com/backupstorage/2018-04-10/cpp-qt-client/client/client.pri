QT += network

HEADERS += \
# Models
    $${PWD}/OAIBackupObject.h \
    $${PWD}/OAIChunk.h \
    $${PWD}/OAIDataChecksumAlgorithm.h \
    $${PWD}/OAIGetChunkOutput.h \
    $${PWD}/OAIGetObjectMetadataOutput.h \
    $${PWD}/OAIListChunksOutput.h \
    $${PWD}/OAIListObjectsOutput.h \
    $${PWD}/OAINotifyObjectCompleteInput.h \
    $${PWD}/OAINotifyObjectCompleteOutput.h \
    $${PWD}/OAINotifyObjectComplete_request.h \
    $${PWD}/OAIPutChunkInput.h \
    $${PWD}/OAIPutChunkOutput.h \
    $${PWD}/OAIPutChunk_request.h \
    $${PWD}/OAIPutObjectInput.h \
    $${PWD}/OAIPutObjectOutput.h \
    $${PWD}/OAIPutObject_request.h \
    $${PWD}/OAIStartObjectInput.h \
    $${PWD}/OAIStartObjectOutput.h \
    $${PWD}/OAIStartObject_request.h \
    $${PWD}/OAISummaryChecksumAlgorithm.h \
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
    $${PWD}/OAIBackupObject.cpp \
    $${PWD}/OAIChunk.cpp \
    $${PWD}/OAIDataChecksumAlgorithm.cpp \
    $${PWD}/OAIGetChunkOutput.cpp \
    $${PWD}/OAIGetObjectMetadataOutput.cpp \
    $${PWD}/OAIListChunksOutput.cpp \
    $${PWD}/OAIListObjectsOutput.cpp \
    $${PWD}/OAINotifyObjectCompleteInput.cpp \
    $${PWD}/OAINotifyObjectCompleteOutput.cpp \
    $${PWD}/OAINotifyObjectComplete_request.cpp \
    $${PWD}/OAIPutChunkInput.cpp \
    $${PWD}/OAIPutChunkOutput.cpp \
    $${PWD}/OAIPutChunk_request.cpp \
    $${PWD}/OAIPutObjectInput.cpp \
    $${PWD}/OAIPutObjectOutput.cpp \
    $${PWD}/OAIPutObject_request.cpp \
    $${PWD}/OAIStartObjectInput.cpp \
    $${PWD}/OAIStartObjectOutput.cpp \
    $${PWD}/OAIStartObject_request.cpp \
    $${PWD}/OAISummaryChecksumAlgorithm.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
