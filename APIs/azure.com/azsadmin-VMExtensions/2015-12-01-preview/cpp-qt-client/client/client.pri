QT += network

HEADERS += \
# Models
    $${PWD}/OAIAzureBlob.h \
    $${PWD}/OAIVMExtension.h \
    $${PWD}/OAIVMExtensionParameters.h \
    $${PWD}/OAIVMExtensionProperties.h \
# APIs
    $${PWD}/OAIVMExtensionsApi.h \
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
    $${PWD}/OAIAzureBlob.cpp \
    $${PWD}/OAIVMExtension.cpp \
    $${PWD}/OAIVMExtensionParameters.cpp \
    $${PWD}/OAIVMExtensionProperties.cpp \
# APIs
    $${PWD}/OAIVMExtensionsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
