QT += network

HEADERS += \
# Models
    $${PWD}/OAIErrorDefinition.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIPolicyMetadata.h \
    $${PWD}/OAIPolicyMetadataCollection.h \
    $${PWD}/OAIPolicyMetadataProperties.h \
    $${PWD}/OAIPolicyMetadataSlimProperties.h \
    $${PWD}/OAISlimPolicyMetadata.h \
    $${PWD}/OAITypedErrorInfo.h \
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
    $${PWD}/OAIErrorDefinition.cpp \
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAIPolicyMetadata.cpp \
    $${PWD}/OAIPolicyMetadataCollection.cpp \
    $${PWD}/OAIPolicyMetadataProperties.cpp \
    $${PWD}/OAIPolicyMetadataSlimProperties.cpp \
    $${PWD}/OAISlimPolicyMetadata.cpp \
    $${PWD}/OAITypedErrorInfo.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
