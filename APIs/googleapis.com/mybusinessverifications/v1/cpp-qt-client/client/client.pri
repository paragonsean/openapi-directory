QT += network

HEADERS += \
# Models
    $${PWD}/OAIAddressVerificationData.h \
    $${PWD}/OAICompleteVerificationRequest.h \
    $${PWD}/OAICompleteVerificationResponse.h \
    $${PWD}/OAIComplyWithGuidelines.h \
    $${PWD}/OAIEmailVerificationData.h \
    $${PWD}/OAIFetchVerificationOptionsRequest.h \
    $${PWD}/OAIFetchVerificationOptionsResponse.h \
    $${PWD}/OAIListVerificationsResponse.h \
    $${PWD}/OAIPostalAddress.h \
    $${PWD}/OAIServiceBusinessContext.h \
    $${PWD}/OAIVerification.h \
    $${PWD}/OAIVerificationOption.h \
    $${PWD}/OAIVerificationToken.h \
    $${PWD}/OAIVerify.h \
    $${PWD}/OAIVerifyLocationRequest.h \
    $${PWD}/OAIVerifyLocationResponse.h \
    $${PWD}/OAIVoiceOfMerchantState.h \
# APIs
    $${PWD}/OAILocationsApi.h \
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
    $${PWD}/OAIAddressVerificationData.cpp \
    $${PWD}/OAICompleteVerificationRequest.cpp \
    $${PWD}/OAICompleteVerificationResponse.cpp \
    $${PWD}/OAIComplyWithGuidelines.cpp \
    $${PWD}/OAIEmailVerificationData.cpp \
    $${PWD}/OAIFetchVerificationOptionsRequest.cpp \
    $${PWD}/OAIFetchVerificationOptionsResponse.cpp \
    $${PWD}/OAIListVerificationsResponse.cpp \
    $${PWD}/OAIPostalAddress.cpp \
    $${PWD}/OAIServiceBusinessContext.cpp \
    $${PWD}/OAIVerification.cpp \
    $${PWD}/OAIVerificationOption.cpp \
    $${PWD}/OAIVerificationToken.cpp \
    $${PWD}/OAIVerify.cpp \
    $${PWD}/OAIVerifyLocationRequest.cpp \
    $${PWD}/OAIVerifyLocationResponse.cpp \
    $${PWD}/OAIVoiceOfMerchantState.cpp \
# APIs
    $${PWD}/OAILocationsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
