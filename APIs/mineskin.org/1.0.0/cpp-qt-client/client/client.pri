QT += network

HEADERS += \
# Models
    $${PWD}/OAIGenerateOptions.h \
    $${PWD}/OAIPartialSkinInfo.h \
    $${PWD}/OAISkinData.h \
    $${PWD}/OAISkinInfo.h \
    $${PWD}/OAIStats.h \
    $${PWD}/OAITextureInfo.h \
    $${PWD}/OAIUserValidation.h \
    $${PWD}/OAI_generate_upload_post_200_response.h \
    $${PWD}/OAI_generate_upload_post_400_response.h \
    $${PWD}/OAI_generate_upload_post_429_response.h \
    $${PWD}/OAI_generate_url_post_request.h \
    $${PWD}/OAI_generate_user_post_request.h \
    $${PWD}/OAI_get_delay_get_200_response.h \
    $${PWD}/OAI_get_list__page__get_200_response.h \
    $${PWD}/OAI_get_list__page__get_200_response_page.h \
# APIs
    $${PWD}/OAIGenerateApi.h \
    $${PWD}/OAIGetApi.h \
    $${PWD}/OAIUtilApi.h \
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
    $${PWD}/OAIGenerateOptions.cpp \
    $${PWD}/OAIPartialSkinInfo.cpp \
    $${PWD}/OAISkinData.cpp \
    $${PWD}/OAISkinInfo.cpp \
    $${PWD}/OAIStats.cpp \
    $${PWD}/OAITextureInfo.cpp \
    $${PWD}/OAIUserValidation.cpp \
    $${PWD}/OAI_generate_upload_post_200_response.cpp \
    $${PWD}/OAI_generate_upload_post_400_response.cpp \
    $${PWD}/OAI_generate_upload_post_429_response.cpp \
    $${PWD}/OAI_generate_url_post_request.cpp \
    $${PWD}/OAI_generate_user_post_request.cpp \
    $${PWD}/OAI_get_delay_get_200_response.cpp \
    $${PWD}/OAI_get_list__page__get_200_response.cpp \
    $${PWD}/OAI_get_list__page__get_200_response_page.cpp \
# APIs
    $${PWD}/OAIGenerateApi.cpp \
    $${PWD}/OAIGetApi.cpp \
    $${PWD}/OAIUtilApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
