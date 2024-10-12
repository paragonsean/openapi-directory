QT += network

HEADERS += \
# Models
    $${PWD}/OAIList_and_search_media_items_200_response.h \
    $${PWD}/OAIList_and_search_media_items_200_response__embedded.h \
    $${PWD}/OAIList_and_search_media_items_200_response__links.h \
    $${PWD}/OAIList_and_search_media_items_200_response__links_first.h \
    $${PWD}/OAIMedia.h \
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
    $${PWD}/OAIList_and_search_media_items_200_response.cpp \
    $${PWD}/OAIList_and_search_media_items_200_response__embedded.cpp \
    $${PWD}/OAIList_and_search_media_items_200_response__links.cpp \
    $${PWD}/OAIList_and_search_media_items_200_response__links_first.cpp \
    $${PWD}/OAIMedia.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
