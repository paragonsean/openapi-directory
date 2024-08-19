QT += network

HEADERS += \
# Models
    $${PWD}/OAIDataWarehouseUserActivities.h \
    $${PWD}/OAIDataWarehouseUserActivitiesProperties.h \
# APIs
    $${PWD}/OAIDataWarehouseUserActivitiesApi.h \
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
    $${PWD}/OAIDataWarehouseUserActivities.cpp \
    $${PWD}/OAIDataWarehouseUserActivitiesProperties.cpp \
# APIs
    $${PWD}/OAIDataWarehouseUserActivitiesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
