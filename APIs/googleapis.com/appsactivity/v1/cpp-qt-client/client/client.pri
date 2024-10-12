QT += network

HEADERS += \
# Models
    $${PWD}/OAIActivity.h \
    $${PWD}/OAIEvent.h \
    $${PWD}/OAIListActivitiesResponse.h \
    $${PWD}/OAIMove.h \
    $${PWD}/OAIParent.h \
    $${PWD}/OAIPermission.h \
    $${PWD}/OAIPermissionChange.h \
    $${PWD}/OAIPhoto.h \
    $${PWD}/OAIRename.h \
    $${PWD}/OAITarget.h \
    $${PWD}/OAIUser.h \
# APIs
    $${PWD}/OAIActivitiesApi.h \
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
    $${PWD}/OAIActivity.cpp \
    $${PWD}/OAIEvent.cpp \
    $${PWD}/OAIListActivitiesResponse.cpp \
    $${PWD}/OAIMove.cpp \
    $${PWD}/OAIParent.cpp \
    $${PWD}/OAIPermission.cpp \
    $${PWD}/OAIPermissionChange.cpp \
    $${PWD}/OAIPhoto.cpp \
    $${PWD}/OAIRename.cpp \
    $${PWD}/OAITarget.cpp \
    $${PWD}/OAIUser.cpp \
# APIs
    $${PWD}/OAIActivitiesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
