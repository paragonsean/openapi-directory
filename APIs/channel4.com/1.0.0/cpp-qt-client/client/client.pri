QT += network

HEADERS += \
# Models
    $${PWD}/OAIAtom.h \
    $${PWD}/OAICommonAttributes.h \
    $${PWD}/OAIKnownRelCodeType.h \
    $${PWD}/OAITextTypeType.h \
# APIs
    $${PWD}/OAIDiscoveryresourcesApi.h \
    $${PWD}/OAIMetadataresourcesApi.h \
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
    $${PWD}/OAIAtom.cpp \
    $${PWD}/OAICommonAttributes.cpp \
    $${PWD}/OAIKnownRelCodeType.cpp \
    $${PWD}/OAITextTypeType.cpp \
# APIs
    $${PWD}/OAIDiscoveryresourcesApi.cpp \
    $${PWD}/OAIMetadataresourcesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
