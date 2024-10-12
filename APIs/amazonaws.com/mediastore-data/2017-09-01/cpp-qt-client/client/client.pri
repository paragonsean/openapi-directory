QT += network

HEADERS += \
# Models
    $${PWD}/OAIGetObjectResponse.h \
    $${PWD}/OAIItem.h \
    $${PWD}/OAIItemType.h \
    $${PWD}/OAIListItemsResponse.h \
    $${PWD}/OAIPutObjectRequest.h \
    $${PWD}/OAIPutObjectResponse.h \
    $${PWD}/OAIPutObject_request.h \
    $${PWD}/OAIStorageClass.h \
    $${PWD}/OAIUploadAvailability.h \
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
    $${PWD}/OAIGetObjectResponse.cpp \
    $${PWD}/OAIItem.cpp \
    $${PWD}/OAIItemType.cpp \
    $${PWD}/OAIListItemsResponse.cpp \
    $${PWD}/OAIPutObjectRequest.cpp \
    $${PWD}/OAIPutObjectResponse.cpp \
    $${PWD}/OAIPutObject_request.cpp \
    $${PWD}/OAIStorageClass.cpp \
    $${PWD}/OAIUploadAvailability.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
