QT += network

HEADERS += \
# Models
    $${PWD}/OAICritic.h \
    $${PWD}/OAICritic_multimedia.h \
    $${PWD}/OAICritic_multimedia_resource.h \
    $${PWD}/OAIMovie.h \
    $${PWD}/OAIMovie_link.h \
    $${PWD}/OAIMovie_multimedia.h \
    $${PWD}/OAIMovie_multimedia_resource.h \
    $${PWD}/OAI_critics__resource_type__json_get_200_response.h \
    $${PWD}/OAI_reviews_search_json_get_200_response.h \
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
    $${PWD}/OAICritic.cpp \
    $${PWD}/OAICritic_multimedia.cpp \
    $${PWD}/OAICritic_multimedia_resource.cpp \
    $${PWD}/OAIMovie.cpp \
    $${PWD}/OAIMovie_link.cpp \
    $${PWD}/OAIMovie_multimedia.cpp \
    $${PWD}/OAIMovie_multimedia_resource.cpp \
    $${PWD}/OAI_critics__resource_type__json_get_200_response.cpp \
    $${PWD}/OAI_reviews_search_json_get_200_response.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
