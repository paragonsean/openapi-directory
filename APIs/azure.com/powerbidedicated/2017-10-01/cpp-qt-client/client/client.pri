QT += network

HEADERS += \
# Models
    $${PWD}/OAICheckCapacityNameAvailabilityParameters.h \
    $${PWD}/OAICheckCapacityNameAvailabilityResult.h \
    $${PWD}/OAIDedicatedCapacities.h \
    $${PWD}/OAIDedicatedCapacity.h \
    $${PWD}/OAIDedicatedCapacityAdministrators.h \
    $${PWD}/OAIDedicatedCapacityMutableProperties.h \
    $${PWD}/OAIDedicatedCapacityProperties.h \
    $${PWD}/OAIDedicatedCapacityUpdateParameters.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIOperationListResult.h \
    $${PWD}/OAIOperation_display.h \
    $${PWD}/OAIResource.h \
    $${PWD}/OAIResourceSku.h \
    $${PWD}/OAISkuDetailsForExistingResource.h \
    $${PWD}/OAISkuEnumerationForExistingResourceResult.h \
    $${PWD}/OAISkuEnumerationForNewResourceResult.h \
# APIs
    $${PWD}/OAICapacitiesApi.h \
    $${PWD}/OAIDefaultApi.h \
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
    $${PWD}/OAICheckCapacityNameAvailabilityParameters.cpp \
    $${PWD}/OAICheckCapacityNameAvailabilityResult.cpp \
    $${PWD}/OAIDedicatedCapacities.cpp \
    $${PWD}/OAIDedicatedCapacity.cpp \
    $${PWD}/OAIDedicatedCapacityAdministrators.cpp \
    $${PWD}/OAIDedicatedCapacityMutableProperties.cpp \
    $${PWD}/OAIDedicatedCapacityProperties.cpp \
    $${PWD}/OAIDedicatedCapacityUpdateParameters.cpp \
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAIOperationListResult.cpp \
    $${PWD}/OAIOperation_display.cpp \
    $${PWD}/OAIResource.cpp \
    $${PWD}/OAIResourceSku.cpp \
    $${PWD}/OAISkuDetailsForExistingResource.cpp \
    $${PWD}/OAISkuEnumerationForExistingResourceResult.cpp \
    $${PWD}/OAISkuEnumerationForNewResourceResult.cpp \
# APIs
    $${PWD}/OAICapacitiesApi.cpp \
    $${PWD}/OAIDefaultApi.cpp \
    $${PWD}/OAIOperationsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
