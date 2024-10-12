QT += network

HEADERS += \
# Models
    $${PWD}/OAIItem.h \
    $${PWD}/OAIItemGroup.h \
    $${PWD}/OAIItemGroupResponse.h \
    $${PWD}/OAIItemPriority.h \
    $${PWD}/OAIItemPriorityResponse.h \
    $${PWD}/OAIItemResponse.h \
    $${PWD}/OAIItemSnapshot.h \
    $${PWD}/OAIItemSnapshotResponse.h \
# APIs
    $${PWD}/OAIItemApi.h \
    $${PWD}/OAIItemGroupApi.h \
    $${PWD}/OAIItemPriorityApi.h \
    $${PWD}/OAIItemSnapshotApi.h \
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
    $${PWD}/OAIItem.cpp \
    $${PWD}/OAIItemGroup.cpp \
    $${PWD}/OAIItemGroupResponse.cpp \
    $${PWD}/OAIItemPriority.cpp \
    $${PWD}/OAIItemPriorityResponse.cpp \
    $${PWD}/OAIItemResponse.cpp \
    $${PWD}/OAIItemSnapshot.cpp \
    $${PWD}/OAIItemSnapshotResponse.cpp \
# APIs
    $${PWD}/OAIItemApi.cpp \
    $${PWD}/OAIItemGroupApi.cpp \
    $${PWD}/OAIItemPriorityApi.cpp \
    $${PWD}/OAIItemSnapshotApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
