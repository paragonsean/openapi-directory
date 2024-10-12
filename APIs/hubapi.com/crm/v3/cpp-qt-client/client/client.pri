QT += network

HEADERS += \
# Models
    $${PWD}/OAIActionConfirmationBody.h \
    $${PWD}/OAIActionHookActionBody.h \
    $${PWD}/OAICardActions.h \
    $${PWD}/OAICardCreateRequest.h \
    $${PWD}/OAICardDisplayBody.h \
    $${PWD}/OAICardDisplayProperty.h \
    $${PWD}/OAICardFetchBody.h \
    $${PWD}/OAICardFetchBodyPatch.h \
    $${PWD}/OAICardListResponse.h \
    $${PWD}/OAICardObjectTypeBody.h \
    $${PWD}/OAICardPatchRequest.h \
    $${PWD}/OAICardResponse.h \
    $${PWD}/OAIDisplayOption.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIErrorDetail.h \
    $${PWD}/OAIIFrameActionBody.h \
    $${PWD}/OAIIntegratorCardPayloadResponse.h \
    $${PWD}/OAIIntegratorObjectResult.h \
    $${PWD}/OAIIntegratorObjectResult_actions_inner.h \
    $${PWD}/OAIObjectToken.h \
    $${PWD}/OAITopLevelActions.h \
# APIs
    $${PWD}/OAICardsApi.h \
    $${PWD}/OAISampleResponseApi.h \
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
    $${PWD}/OAIActionConfirmationBody.cpp \
    $${PWD}/OAIActionHookActionBody.cpp \
    $${PWD}/OAICardActions.cpp \
    $${PWD}/OAICardCreateRequest.cpp \
    $${PWD}/OAICardDisplayBody.cpp \
    $${PWD}/OAICardDisplayProperty.cpp \
    $${PWD}/OAICardFetchBody.cpp \
    $${PWD}/OAICardFetchBodyPatch.cpp \
    $${PWD}/OAICardListResponse.cpp \
    $${PWD}/OAICardObjectTypeBody.cpp \
    $${PWD}/OAICardPatchRequest.cpp \
    $${PWD}/OAICardResponse.cpp \
    $${PWD}/OAIDisplayOption.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIErrorDetail.cpp \
    $${PWD}/OAIIFrameActionBody.cpp \
    $${PWD}/OAIIntegratorCardPayloadResponse.cpp \
    $${PWD}/OAIIntegratorObjectResult.cpp \
    $${PWD}/OAIIntegratorObjectResult_actions_inner.cpp \
    $${PWD}/OAIObjectToken.cpp \
    $${PWD}/OAITopLevelActions.cpp \
# APIs
    $${PWD}/OAICardsApi.cpp \
    $${PWD}/OAISampleResponseApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
