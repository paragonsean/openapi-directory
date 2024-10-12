QT += network

HEADERS += \
# Models
    $${PWD}/OAIAnswer.h \
    $${PWD}/OAICreativeWork.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIIdentifiable.h \
    $${PWD}/OAIImageObject.h \
    $${PWD}/OAIMediaObject.h \
    $${PWD}/OAIPivotSuggestions.h \
    $${PWD}/OAIQuery.h \
    $${PWD}/OAIQueryContext.h \
    $${PWD}/OAIResponse.h \
    $${PWD}/OAIResponseBase.h \
    $${PWD}/OAISearchResultsAnswer.h \
    $${PWD}/OAIThing.h \
    $${PWD}/OAITrendingVideos.h \
    $${PWD}/OAITrendingVideosCategory.h \
    $${PWD}/OAITrendingVideosSubcategory.h \
    $${PWD}/OAITrendingVideosTile.h \
    $${PWD}/OAIVideoDetails.h \
    $${PWD}/OAIVideoObject.h \
    $${PWD}/OAIVideos.h \
    $${PWD}/OAIVideosModule.h \
# APIs
    $${PWD}/OAIVideoDetailSearchApi.h \
    $${PWD}/OAIVideoSearchApi.h \
    $${PWD}/OAIVideoTrendingSearchApi.h \
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
    $${PWD}/OAICreativeWork.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAIIdentifiable.cpp \
    $${PWD}/OAIImageObject.cpp \
    $${PWD}/OAIMediaObject.cpp \
    $${PWD}/OAIPivotSuggestions.cpp \
    $${PWD}/OAIQuery.cpp \
    $${PWD}/OAIQueryContext.cpp \
    $${PWD}/OAIResponse.cpp \
    $${PWD}/OAIResponseBase.cpp \
    $${PWD}/OAISearchResultsAnswer.cpp \
    $${PWD}/OAIThing.cpp \
    $${PWD}/OAITrendingVideos.cpp \
    $${PWD}/OAITrendingVideosCategory.cpp \
    $${PWD}/OAITrendingVideosSubcategory.cpp \
    $${PWD}/OAITrendingVideosTile.cpp \
    $${PWD}/OAIVideoDetails.cpp \
    $${PWD}/OAIVideoObject.cpp \
    $${PWD}/OAIVideos.cpp \
    $${PWD}/OAIVideosModule.cpp \
# APIs
    $${PWD}/OAIVideoDetailSearchApi.cpp \
    $${PWD}/OAIVideoSearchApi.cpp \
    $${PWD}/OAIVideoTrendingSearchApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
