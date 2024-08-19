QT += network

HEADERS += \
# Models
    $${PWD}/OAIApiEntityReference.h \
    $${PWD}/OAIDedicatedHsm.h \
    $${PWD}/OAIDedicatedHsmError.h \
    $${PWD}/OAIDedicatedHsmListResult.h \
    $${PWD}/OAIDedicatedHsmPatchParameters.h \
    $${PWD}/OAIDedicatedHsmProperties.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAINetworkInterface.h \
    $${PWD}/OAINetworkProfile.h \
    $${PWD}/OAIResource.h \
    $${PWD}/OAIResourceListResult.h \
    $${PWD}/OAISku.h \
# APIs
    $${PWD}/OAIDedicatedHsmsApi.h \
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
    $${PWD}/OAIApiEntityReference.cpp \
    $${PWD}/OAIDedicatedHsm.cpp \
    $${PWD}/OAIDedicatedHsmError.cpp \
    $${PWD}/OAIDedicatedHsmListResult.cpp \
    $${PWD}/OAIDedicatedHsmPatchParameters.cpp \
    $${PWD}/OAIDedicatedHsmProperties.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAINetworkInterface.cpp \
    $${PWD}/OAINetworkProfile.cpp \
    $${PWD}/OAIResource.cpp \
    $${PWD}/OAIResourceListResult.cpp \
    $${PWD}/OAISku.cpp \
# APIs
    $${PWD}/OAIDedicatedHsmsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
