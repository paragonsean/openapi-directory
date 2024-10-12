QT += network

HEADERS += \
# Models
    $${PWD}/OAICategoryList.h \
    $${PWD}/OAICategoryListCategoriesItem.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAILanguageItem.h \
    $${PWD}/OAILanguageList.h \
    $${PWD}/OAIPodcastEpisodeList.h \
    $${PWD}/OAIPodcastEpisodeListEpisodesItem.h \
    $${PWD}/OAIPodcastEpisodeListEpisodesItem_play.h \
    $${PWD}/OAIPodcastList.h \
    $${PWD}/OAIPodcastListPodcastsItem.h \
    $${PWD}/OAIPodcastListPodcastsItem_category.h \
    $${PWD}/OAISingleCategory.h \
    $${PWD}/OAISingleCategoryCategory.h \
    $${PWD}/OAISinglePodcast.h \
    $${PWD}/OAISinglePodcastPodcast.h \
# APIs
    $${PWD}/OAICategoryApi.h \
    $${PWD}/OAIPodcastApi.h \
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
    $${PWD}/OAICategoryList.cpp \
    $${PWD}/OAICategoryListCategoriesItem.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAILanguageItem.cpp \
    $${PWD}/OAILanguageList.cpp \
    $${PWD}/OAIPodcastEpisodeList.cpp \
    $${PWD}/OAIPodcastEpisodeListEpisodesItem.cpp \
    $${PWD}/OAIPodcastEpisodeListEpisodesItem_play.cpp \
    $${PWD}/OAIPodcastList.cpp \
    $${PWD}/OAIPodcastListPodcastsItem.cpp \
    $${PWD}/OAIPodcastListPodcastsItem_category.cpp \
    $${PWD}/OAISingleCategory.cpp \
    $${PWD}/OAISingleCategoryCategory.cpp \
    $${PWD}/OAISinglePodcast.cpp \
    $${PWD}/OAISinglePodcastPodcast.cpp \
# APIs
    $${PWD}/OAICategoryApi.cpp \
    $${PWD}/OAIPodcastApi.cpp \
    $${PWD}/OAIUtilApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
