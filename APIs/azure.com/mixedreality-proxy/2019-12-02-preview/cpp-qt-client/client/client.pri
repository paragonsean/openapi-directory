QT += network

HEADERS += \
# Models
    $${PWD}/OAICheckNameAvailabilityRequest.h \
    $${PWD}/OAICheckNameAvailabilityResponse.h \
    $${PWD}/OAINameAvailability.h \
    $${PWD}/OAINameUnavailableReason.h \
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIOperationDisplay.h \
    $${PWD}/OAIOperationPage.h \
    $${PWD}/OAIOperations_List_default_response.h \
# APIs
    $${PWD}/OAIProxyApi.h \
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
    $${PWD}/OAICheckNameAvailabilityRequest.cpp \
    $${PWD}/OAICheckNameAvailabilityResponse.cpp \
    $${PWD}/OAINameAvailability.cpp \
    $${PWD}/OAINameUnavailableReason.cpp \
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAIOperationDisplay.cpp \
    $${PWD}/OAIOperationPage.cpp \
    $${PWD}/OAIOperations_List_default_response.cpp \
# APIs
    $${PWD}/OAIProxyApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
