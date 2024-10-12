QT += network

HEADERS += \
# Models
    $${PWD}/OAIAPIResponseSimilarity.h \
    $${PWD}/OAIAPIResponseSimilarity_response.h \
    $${PWD}/OAIAPIResponseSimilarity_response_similarity_list_inner.h \
    $${PWD}/OAIAPIResponseSong.h \
    $${PWD}/OAIAPIResponseSong_response.h \
    $${PWD}/OAIAPIResponseSong_response_results_inner.h \
    $${PWD}/OAISrc_searchly_api_v1_controllers_similarity_by_content_request.h \
# APIs
    $${PWD}/OAISimilarityApi.h \
    $${PWD}/OAISongApi.h \
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
    $${PWD}/OAIAPIResponseSimilarity.cpp \
    $${PWD}/OAIAPIResponseSimilarity_response.cpp \
    $${PWD}/OAIAPIResponseSimilarity_response_similarity_list_inner.cpp \
    $${PWD}/OAIAPIResponseSong.cpp \
    $${PWD}/OAIAPIResponseSong_response.cpp \
    $${PWD}/OAIAPIResponseSong_response_results_inner.cpp \
    $${PWD}/OAISrc_searchly_api_v1_controllers_similarity_by_content_request.cpp \
# APIs
    $${PWD}/OAISimilarityApi.cpp \
    $${PWD}/OAISongApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
