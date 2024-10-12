QT += network

HEADERS += \
# Models
    $${PWD}/OAIArticle.h \
    $${PWD}/OAIContentProCompany.h \
    $${PWD}/OAIContentProSnippets.h \
    $${PWD}/OAIInputCompany.h \
    $${PWD}/OAISimilarCompany.h \
    $${PWD}/OAISimilarCompanySearch.h \
    $${PWD}/OAISnippet.h \
    $${PWD}/OAI_contentpro_search_get_200_response.h \
    $${PWD}/OAI_contentpro_search_get_200_response_data_inner.h \
    $${PWD}/OAI_contentpro_similar_text_post_request.h \
    $${PWD}/OAI_search_get_200_response.h \
    $${PWD}/OAI_similar_get_200_response.h \
# APIs
    $${PWD}/OAIContentproSearchApi.h \
    $${PWD}/OAIContentproSimilarTextApi.h \
    $${PWD}/OAISearchApi.h \
    $${PWD}/OAISimilarApi.h \
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
    $${PWD}/OAIArticle.cpp \
    $${PWD}/OAIContentProCompany.cpp \
    $${PWD}/OAIContentProSnippets.cpp \
    $${PWD}/OAIInputCompany.cpp \
    $${PWD}/OAISimilarCompany.cpp \
    $${PWD}/OAISimilarCompanySearch.cpp \
    $${PWD}/OAISnippet.cpp \
    $${PWD}/OAI_contentpro_search_get_200_response.cpp \
    $${PWD}/OAI_contentpro_search_get_200_response_data_inner.cpp \
    $${PWD}/OAI_contentpro_similar_text_post_request.cpp \
    $${PWD}/OAI_search_get_200_response.cpp \
    $${PWD}/OAI_similar_get_200_response.cpp \
# APIs
    $${PWD}/OAIContentproSearchApi.cpp \
    $${PWD}/OAIContentproSimilarTextApi.cpp \
    $${PWD}/OAISearchApi.cpp \
    $${PWD}/OAISimilarApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
