QT += network

HEADERS += \
# Models
    $${PWD}/OAIAnswer.h \
    $${PWD}/OAIArticle.h \
    $${PWD}/OAICreativeWork.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIIdentifiable.h \
    $${PWD}/OAIImageObject.h \
    $${PWD}/OAIMediaObject.h \
    $${PWD}/OAINews.h \
    $${PWD}/OAINewsArticle.h \
    $${PWD}/OAINewsTopic.h \
    $${PWD}/OAIOrganization.h \
    $${PWD}/OAIQuery.h \
    $${PWD}/OAIResponse.h \
    $${PWD}/OAIResponseBase.h \
    $${PWD}/OAISearchResultsAnswer.h \
    $${PWD}/OAIThing.h \
    $${PWD}/OAITrendingTopics.h \
    $${PWD}/OAIVideoObject.h \
# APIs
    $${PWD}/OAINewsCategoryApi.h \
    $${PWD}/OAINewsSearchApi.h \
    $${PWD}/OAINewsTrendingTopicsApi.h \
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
    $${PWD}/OAIAnswer.cpp \
    $${PWD}/OAIArticle.cpp \
    $${PWD}/OAICreativeWork.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAIIdentifiable.cpp \
    $${PWD}/OAIImageObject.cpp \
    $${PWD}/OAIMediaObject.cpp \
    $${PWD}/OAINews.cpp \
    $${PWD}/OAINewsArticle.cpp \
    $${PWD}/OAINewsTopic.cpp \
    $${PWD}/OAIOrganization.cpp \
    $${PWD}/OAIQuery.cpp \
    $${PWD}/OAIResponse.cpp \
    $${PWD}/OAIResponseBase.cpp \
    $${PWD}/OAISearchResultsAnswer.cpp \
    $${PWD}/OAIThing.cpp \
    $${PWD}/OAITrendingTopics.cpp \
    $${PWD}/OAIVideoObject.cpp \
# APIs
    $${PWD}/OAINewsCategoryApi.cpp \
    $${PWD}/OAINewsSearchApi.cpp \
    $${PWD}/OAINewsTrendingTopicsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
