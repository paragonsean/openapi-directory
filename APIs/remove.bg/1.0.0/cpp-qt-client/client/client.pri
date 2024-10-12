QT += network

HEADERS += \
# Models
    $${PWD}/OAIAuthFailed.h \
    $${PWD}/OAIAuthFailed_errors_inner.h \
    $${PWD}/OAIImprovementProgramJson.h \
    $${PWD}/OAIImprovementProgramJsonResponse.h \
    $${PWD}/OAIRateLimit.h \
    $${PWD}/OAIRateLimit_errors_inner.h \
    $${PWD}/OAIRemoveBgJson.h \
    $${PWD}/OAIRemoveBgJsonResponse.h \
    $${PWD}/OAIRemoveBgJsonResponse_data.h \
    $${PWD}/OAI_account_get_200_response.h \
    $${PWD}/OAI_account_get_200_response_data.h \
    $${PWD}/OAI_account_get_200_response_data_attributes.h \
    $${PWD}/OAI_account_get_200_response_data_attributes_api.h \
    $${PWD}/OAI_account_get_200_response_data_attributes_credits.h \
    $${PWD}/OAI_improve_post_400_response.h \
    $${PWD}/OAI_improve_post_400_response_errors_inner.h \
    $${PWD}/OAI_removebg_post_400_response.h \
    $${PWD}/OAI_removebg_post_400_response_errors_inner.h \
    $${PWD}/OAI_removebg_post_402_response.h \
    $${PWD}/OAI_removebg_post_402_response_errors_inner.h \
# APIs
    $${PWD}/OAIBackgroundRemovalApi.h \
    $${PWD}/OAIFetchAccountInfoApi.h \
    $${PWD}/OAIImprovementProgramApi.h \
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
    $${PWD}/OAIAuthFailed.cpp \
    $${PWD}/OAIAuthFailed_errors_inner.cpp \
    $${PWD}/OAIImprovementProgramJson.cpp \
    $${PWD}/OAIImprovementProgramJsonResponse.cpp \
    $${PWD}/OAIRateLimit.cpp \
    $${PWD}/OAIRateLimit_errors_inner.cpp \
    $${PWD}/OAIRemoveBgJson.cpp \
    $${PWD}/OAIRemoveBgJsonResponse.cpp \
    $${PWD}/OAIRemoveBgJsonResponse_data.cpp \
    $${PWD}/OAI_account_get_200_response.cpp \
    $${PWD}/OAI_account_get_200_response_data.cpp \
    $${PWD}/OAI_account_get_200_response_data_attributes.cpp \
    $${PWD}/OAI_account_get_200_response_data_attributes_api.cpp \
    $${PWD}/OAI_account_get_200_response_data_attributes_credits.cpp \
    $${PWD}/OAI_improve_post_400_response.cpp \
    $${PWD}/OAI_improve_post_400_response_errors_inner.cpp \
    $${PWD}/OAI_removebg_post_400_response.cpp \
    $${PWD}/OAI_removebg_post_400_response_errors_inner.cpp \
    $${PWD}/OAI_removebg_post_402_response.cpp \
    $${PWD}/OAI_removebg_post_402_response_errors_inner.cpp \
# APIs
    $${PWD}/OAIBackgroundRemovalApi.cpp \
    $${PWD}/OAIFetchAccountInfoApi.cpp \
    $${PWD}/OAIImprovementProgramApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
