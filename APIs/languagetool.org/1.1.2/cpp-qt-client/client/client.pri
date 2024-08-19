QT += network

HEADERS += \
# Models
    $${PWD}/OAI_check_post_200_response.h \
    $${PWD}/OAI_check_post_200_response_language.h \
    $${PWD}/OAI_check_post_200_response_language_detectedLanguage.h \
    $${PWD}/OAI_check_post_200_response_matches_inner.h \
    $${PWD}/OAI_check_post_200_response_matches_inner_context.h \
    $${PWD}/OAI_check_post_200_response_matches_inner_replacements_inner.h \
    $${PWD}/OAI_check_post_200_response_matches_inner_rule.h \
    $${PWD}/OAI_check_post_200_response_matches_inner_rule_category.h \
    $${PWD}/OAI_check_post_200_response_matches_inner_rule_urls_inner.h \
    $${PWD}/OAI_check_post_200_response_software.h \
    $${PWD}/OAI_languages_get_200_response_inner.h \
    $${PWD}/OAI_words_add_post_200_response.h \
    $${PWD}/OAI_words_delete_post_200_response.h \
    $${PWD}/OAI_words_get_200_response.h \
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
    $${PWD}/OAI_check_post_200_response.cpp \
    $${PWD}/OAI_check_post_200_response_language.cpp \
    $${PWD}/OAI_check_post_200_response_language_detectedLanguage.cpp \
    $${PWD}/OAI_check_post_200_response_matches_inner.cpp \
    $${PWD}/OAI_check_post_200_response_matches_inner_context.cpp \
    $${PWD}/OAI_check_post_200_response_matches_inner_replacements_inner.cpp \
    $${PWD}/OAI_check_post_200_response_matches_inner_rule.cpp \
    $${PWD}/OAI_check_post_200_response_matches_inner_rule_category.cpp \
    $${PWD}/OAI_check_post_200_response_matches_inner_rule_urls_inner.cpp \
    $${PWD}/OAI_check_post_200_response_software.cpp \
    $${PWD}/OAI_languages_get_200_response_inner.cpp \
    $${PWD}/OAI_words_add_post_200_response.cpp \
    $${PWD}/OAI_words_delete_post_200_response.cpp \
    $${PWD}/OAI_words_get_200_response.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
