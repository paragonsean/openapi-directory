QT += network

HEADERS += \
# Models
    $${PWD}/OAIDeletedWebAppCollection.h \
    $${PWD}/OAIDeletedWebAppCollection_value_inner.h \
    $${PWD}/OAIDeletedWebApps_GetDeletedWebAppByLocation_200_response.h \
    $${PWD}/OAIDeletedWebApps_GetDeletedWebAppByLocation_200_response_properties.h \
    $${PWD}/OAIDeletedWebApps_List_default_response.h \
    $${PWD}/OAIDeletedWebApps_List_default_response_error.h \
    $${PWD}/OAIDeletedWebApps_List_default_response_error_details_inner.h \
# APIs
    $${PWD}/OAIDeletedWebAppsApi.h \
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
    $${PWD}/OAIDeletedWebAppCollection.cpp \
    $${PWD}/OAIDeletedWebAppCollection_value_inner.cpp \
    $${PWD}/OAIDeletedWebApps_GetDeletedWebAppByLocation_200_response.cpp \
    $${PWD}/OAIDeletedWebApps_GetDeletedWebAppByLocation_200_response_properties.cpp \
    $${PWD}/OAIDeletedWebApps_List_default_response.cpp \
    $${PWD}/OAIDeletedWebApps_List_default_response_error.cpp \
    $${PWD}/OAIDeletedWebApps_List_default_response_error_details_inner.cpp \
# APIs
    $${PWD}/OAIDeletedWebAppsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
