QT += network

HEADERS += \
# Models
# APIs
    $${PWD}/OAIContractsApi.h \
    $${PWD}/OAIMetadataApi.h \
    $${PWD}/OAINaicsApi.h \
    $${PWD}/OAIVendorApi.h \
    $${PWD}/OAIVendorsApi.h \
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
# APIs
    $${PWD}/OAIContractsApi.cpp \
    $${PWD}/OAIMetadataApi.cpp \
    $${PWD}/OAINaicsApi.cpp \
    $${PWD}/OAIVendorApi.cpp \
    $${PWD}/OAIVendorsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
