QT += network

HEADERS += \
# Models
    $${PWD}/OAIApiError.h \
    $${PWD}/OAICheckNameAvailabilityInput.h \
    $${PWD}/OAIEntityNameAvailabilityCheckOutput.h \
    $${PWD}/OAILocation.h \
    $${PWD}/OAIMediaService.h \
    $${PWD}/OAIMediaServiceCollection.h \
    $${PWD}/OAIMediaServiceProperties.h \
    $${PWD}/OAIODataError.h \
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIOperationCollection.h \
    $${PWD}/OAIOperationDisplay.h \
    $${PWD}/OAIProvider.h \
    $${PWD}/OAIStorageAccount.h \
    $${PWD}/OAISubscriptionMediaService.h \
    $${PWD}/OAISubscriptionMediaServiceCollection.h \
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
    $${PWD}/OAIApiError.cpp \
    $${PWD}/OAICheckNameAvailabilityInput.cpp \
    $${PWD}/OAIEntityNameAvailabilityCheckOutput.cpp \
    $${PWD}/OAILocation.cpp \
    $${PWD}/OAIMediaService.cpp \
    $${PWD}/OAIMediaServiceCollection.cpp \
    $${PWD}/OAIMediaServiceProperties.cpp \
    $${PWD}/OAIODataError.cpp \
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAIOperationCollection.cpp \
    $${PWD}/OAIOperationDisplay.cpp \
    $${PWD}/OAIProvider.cpp \
    $${PWD}/OAIStorageAccount.cpp \
    $${PWD}/OAISubscriptionMediaService.cpp \
    $${PWD}/OAISubscriptionMediaServiceCollection.cpp \
    $${PWD}/OAISyncStorageKeysInput.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
