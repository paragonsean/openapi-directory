QT += network

HEADERS += \
# Models
    $${PWD}/OAIError.h \
    $${PWD}/OAIErrorCode.h \
    $${PWD}/OAIHybridUseBenefitListResult.h \
    $${PWD}/OAIHybridUseBenefitModel.h \
    $${PWD}/OAIHybridUseBenefitProperties.h \
    $${PWD}/OAIOperationDisplay.h \
    $${PWD}/OAIOperationList.h \
    $${PWD}/OAIOperationResponse.h \
    $${PWD}/OAIProvisioningState.h \
    $${PWD}/OAISku.h \
# APIs
    $${PWD}/OAIHybridUseBenefitApi.h \
    $${PWD}/OAIHybridUseBenefitRevisionsApi.h \
    $${PWD}/OAIHybridUseBenefitsApi.h \
    $${PWD}/OAISoftwarePlanApi.h \
    $${PWD}/OAISoftwarePlanOperationsApi.h \
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
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIErrorCode.cpp \
    $${PWD}/OAIHybridUseBenefitListResult.cpp \
    $${PWD}/OAIHybridUseBenefitModel.cpp \
    $${PWD}/OAIHybridUseBenefitProperties.cpp \
    $${PWD}/OAIOperationDisplay.cpp \
    $${PWD}/OAIOperationList.cpp \
    $${PWD}/OAIOperationResponse.cpp \
    $${PWD}/OAIProvisioningState.cpp \
    $${PWD}/OAISku.cpp \
# APIs
    $${PWD}/OAIHybridUseBenefitApi.cpp \
    $${PWD}/OAIHybridUseBenefitRevisionsApi.cpp \
    $${PWD}/OAIHybridUseBenefitsApi.cpp \
    $${PWD}/OAISoftwarePlanApi.cpp \
    $${PWD}/OAISoftwarePlanOperationsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
