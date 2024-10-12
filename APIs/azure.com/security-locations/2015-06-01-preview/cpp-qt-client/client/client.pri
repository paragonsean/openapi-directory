QT += network

HEADERS += \
# Models
    $${PWD}/OAILocations_Get_200_response.h \
    $${PWD}/OAILocations_List_200_response.h \
    $${PWD}/OAILocations_List_200_response_value_inner.h \
    $${PWD}/OAILocations_List_default_response.h \
    $${PWD}/OAILocations_List_default_response_error.h \
# APIs
    $${PWD}/OAILocationsApi.h \
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
    $${PWD}/OAILocations_Get_200_response.cpp \
    $${PWD}/OAILocations_List_200_response.cpp \
    $${PWD}/OAILocations_List_200_response_value_inner.cpp \
    $${PWD}/OAILocations_List_default_response.cpp \
    $${PWD}/OAILocations_List_default_response_error.cpp \
# APIs
    $${PWD}/OAILocationsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
