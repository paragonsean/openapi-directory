QT += network

HEADERS += \
# Models
    $${PWD}/OAIAmount.h \
    $${PWD}/OAICardBin.h \
    $${PWD}/OAICostEstimateAssumptions.h \
    $${PWD}/OAICostEstimateRequest.h \
    $${PWD}/OAICostEstimateResponse.h \
    $${PWD}/OAIDSPublicKeyDetail.h \
    $${PWD}/OAIMerchantDetails.h \
    $${PWD}/OAIRecurring.h \
    $${PWD}/OAIServiceError.h \
    $${PWD}/OAIThreeDS2CardRangeDetail.h \
    $${PWD}/OAIThreeDSAvailabilityRequest.h \
    $${PWD}/OAIThreeDSAvailabilityResponse.h \
# APIs
    $${PWD}/OAIGeneralApi.h \
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
    $${PWD}/OAIAmount.cpp \
    $${PWD}/OAICardBin.cpp \
    $${PWD}/OAICostEstimateAssumptions.cpp \
    $${PWD}/OAICostEstimateRequest.cpp \
    $${PWD}/OAICostEstimateResponse.cpp \
    $${PWD}/OAIDSPublicKeyDetail.cpp \
    $${PWD}/OAIMerchantDetails.cpp \
    $${PWD}/OAIRecurring.cpp \
    $${PWD}/OAIServiceError.cpp \
    $${PWD}/OAIThreeDS2CardRangeDetail.cpp \
    $${PWD}/OAIThreeDSAvailabilityRequest.cpp \
    $${PWD}/OAIThreeDSAvailabilityResponse.cpp \
# APIs
    $${PWD}/OAIGeneralApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
