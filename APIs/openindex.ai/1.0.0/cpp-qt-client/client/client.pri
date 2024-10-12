QT += network

HEADERS += \
# Models
    $${PWD}/OAIDocumentChunkMetadata.h \
    $${PWD}/OAIDocumentChunkWithScore.h \
    $${PWD}/OAIDocumentMetadataFilter.h \
    $${PWD}/OAIHTTPValidationError.h \
    $${PWD}/OAILocation_inner.h \
    $${PWD}/OAIQuery.h \
    $${PWD}/OAIQueryRequest.h \
    $${PWD}/OAIQueryResponse.h \
    $${PWD}/OAIQueryResult.h \
    $${PWD}/OAISource.h \
    $${PWD}/OAIValidationError.h \
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
    $${PWD}/OAIDocumentChunkMetadata.cpp \
    $${PWD}/OAIDocumentChunkWithScore.cpp \
    $${PWD}/OAIDocumentMetadataFilter.cpp \
    $${PWD}/OAIHTTPValidationError.cpp \
    $${PWD}/OAILocation_inner.cpp \
    $${PWD}/OAIQuery.cpp \
    $${PWD}/OAIQueryRequest.cpp \
    $${PWD}/OAIQueryResponse.cpp \
    $${PWD}/OAIQueryResult.cpp \
    $${PWD}/OAISource.cpp \
    $${PWD}/OAIValidationError.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
