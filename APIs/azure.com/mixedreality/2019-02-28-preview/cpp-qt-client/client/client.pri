QT += network

HEADERS += \
# Models
    $${PWD}/OAICheckNameAvailabilityRequest.h \
    $${PWD}/OAICheckNameAvailabilityResponse.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAINameAvailability.h \
    $${PWD}/OAINameUnavailableReason.h \
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIOperationDisplay.h \
    $${PWD}/OAIOperationList.h \
    $${PWD}/OAISpatialAnchorsAccount.h \
    $${PWD}/OAISpatialAnchorsAccountKeyRegenerateRequest.h \
    $${PWD}/OAISpatialAnchorsAccountKeys.h \
    $${PWD}/OAISpatialAnchorsAccountList.h \
    $${PWD}/OAISpatialAnchorsAccountProperties.h \
# APIs
    $${PWD}/OAIKeyApi.h \
    $${PWD}/OAIProxyApi.h \
    $${PWD}/OAIResourceApi.h \
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
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAINameAvailability.cpp \
    $${PWD}/OAINameUnavailableReason.cpp \
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAIOperationDisplay.cpp \
    $${PWD}/OAIOperationList.cpp \
    $${PWD}/OAISpatialAnchorsAccount.cpp \
    $${PWD}/OAISpatialAnchorsAccountKeyRegenerateRequest.cpp \
    $${PWD}/OAISpatialAnchorsAccountKeys.cpp \
    $${PWD}/OAISpatialAnchorsAccountList.cpp \
    $${PWD}/OAISpatialAnchorsAccountProperties.cpp \
# APIs
    $${PWD}/OAIKeyApi.cpp \
    $${PWD}/OAIProxyApi.cpp \
    $${PWD}/OAIResourceApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
