QT += network

HEADERS += \
# Models
    $${PWD}/OAIApp.h \
    $${PWD}/OAIAppListResult.h \
    $${PWD}/OAIAppNameAvailabilityInfo.h \
    $${PWD}/OAIAppPatch.h \
    $${PWD}/OAIAppProperties.h \
    $${PWD}/OAIAppSkuInfo.h \
    $${PWD}/OAIErrorDetails.h \
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIOperationDisplay.h \
    $${PWD}/OAIOperationInputs.h \
    $${PWD}/OAIOperationListResult.h \
    $${PWD}/OAIResource.h \
# APIs
    $${PWD}/OAIAppsApi.h \
    $${PWD}/OAIOperationsApi.h \
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
    $${PWD}/OAIApp.cpp \
    $${PWD}/OAIAppListResult.cpp \
    $${PWD}/OAIAppNameAvailabilityInfo.cpp \
    $${PWD}/OAIAppPatch.cpp \
    $${PWD}/OAIAppProperties.cpp \
    $${PWD}/OAIAppSkuInfo.cpp \
    $${PWD}/OAIErrorDetails.cpp \
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAIOperationDisplay.cpp \
    $${PWD}/OAIOperationInputs.cpp \
    $${PWD}/OAIOperationListResult.cpp \
    $${PWD}/OAIResource.cpp \
# APIs
    $${PWD}/OAIAppsApi.cpp \
    $${PWD}/OAIOperationsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
