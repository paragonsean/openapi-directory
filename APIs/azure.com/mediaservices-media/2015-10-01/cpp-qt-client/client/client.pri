QT += network

HEADERS += \
# Models
    $${PWD}/OAIApiEndpoint.h \
    $${PWD}/OAIApiError.h \
    $${PWD}/OAICheckNameAvailabilityInput.h \
    $${PWD}/OAICheckNameAvailabilityOutput.h \
    $${PWD}/OAIMediaService.h \
    $${PWD}/OAIMediaServiceCollection.h \
    $${PWD}/OAIMediaServiceProperties.h \
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIOperationListResult.h \
    $${PWD}/OAIOperation_display.h \
    $${PWD}/OAIRegenerateKeyInput.h \
    $${PWD}/OAIRegenerateKeyOutput.h \
    $${PWD}/OAIResource.h \
    $${PWD}/OAIResourceType.h \
    $${PWD}/OAIServiceKeys.h \
    $${PWD}/OAIStorageAccount.h \
    $${PWD}/OAISyncStorageKeysInput.h \
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
    $${PWD}/OAIApiEndpoint.cpp \
    $${PWD}/OAIApiError.cpp \
    $${PWD}/OAICheckNameAvailabilityInput.cpp \
    $${PWD}/OAICheckNameAvailabilityOutput.cpp \
    $${PWD}/OAIMediaService.cpp \
    $${PWD}/OAIMediaServiceCollection.cpp \
    $${PWD}/OAIMediaServiceProperties.cpp \
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAIOperationListResult.cpp \
    $${PWD}/OAIOperation_display.cpp \
    $${PWD}/OAIRegenerateKeyInput.cpp \
    $${PWD}/OAIRegenerateKeyOutput.cpp \
    $${PWD}/OAIResource.cpp \
    $${PWD}/OAIResourceType.cpp \
    $${PWD}/OAIServiceKeys.cpp \
    $${PWD}/OAIStorageAccount.cpp \
    $${PWD}/OAISyncStorageKeysInput.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
