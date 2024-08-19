QT += network

HEADERS += \
# Models
    $${PWD}/OAI_search__versionNumber__geometryFilter__ext__post_request.h \
    $${PWD}/OAI_search__versionNumber__geometryFilter__ext__post_request_geometryList_inner.h \
    $${PWD}/OAI_search__versionNumber__geometryFilter__ext__post_request_poiList_inner.h \
    $${PWD}/OAI_search__versionNumber__geometryFilter__ext__post_request_poiList_inner_address.h \
    $${PWD}/OAI_search__versionNumber__geometryFilter__ext__post_request_poiList_inner_poi.h \
    $${PWD}/OAI_search__versionNumber__geometryFilter__ext__post_request_poiList_inner_position.h \
    $${PWD}/OAI_search__versionNumber__geometrySearch__query___ext__post_request.h \
    $${PWD}/OAI_search__versionNumber__routedFilter__position___heading___ext__post_request.h \
    $${PWD}/OAI_search__versionNumber__searchAlongRoute__query___ext__post_request.h \
    $${PWD}/OAI_search__versionNumber__searchAlongRoute__query___ext__post_request_route.h \
# APIs
    $${PWD}/OAIAdditionalDataApi.h \
    $${PWD}/OAIFiltersApi.h \
    $${PWD}/OAIGeocodingApi.h \
    $${PWD}/OAIReverseGeocodingApi.h \
    $${PWD}/OAISearchApi.h \
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
    $${PWD}/OAI_search__versionNumber__geometryFilter__ext__post_request.cpp \
    $${PWD}/OAI_search__versionNumber__geometryFilter__ext__post_request_geometryList_inner.cpp \
    $${PWD}/OAI_search__versionNumber__geometryFilter__ext__post_request_poiList_inner.cpp \
    $${PWD}/OAI_search__versionNumber__geometryFilter__ext__post_request_poiList_inner_address.cpp \
    $${PWD}/OAI_search__versionNumber__geometryFilter__ext__post_request_poiList_inner_poi.cpp \
    $${PWD}/OAI_search__versionNumber__geometryFilter__ext__post_request_poiList_inner_position.cpp \
    $${PWD}/OAI_search__versionNumber__geometrySearch__query___ext__post_request.cpp \
    $${PWD}/OAI_search__versionNumber__routedFilter__position___heading___ext__post_request.cpp \
    $${PWD}/OAI_search__versionNumber__searchAlongRoute__query___ext__post_request.cpp \
    $${PWD}/OAI_search__versionNumber__searchAlongRoute__query___ext__post_request_route.cpp \
# APIs
    $${PWD}/OAIAdditionalDataApi.cpp \
    $${PWD}/OAIFiltersApi.cpp \
    $${PWD}/OAIGeocodingApi.cpp \
    $${PWD}/OAIReverseGeocodingApi.cpp \
    $${PWD}/OAISearchApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
