QT += network

HEADERS += \
# Models
    $${PWD}/OAIAssociation.h \
    $${PWD}/OAIFileObject.h \
    $${PWD}/OAIFiles.h \
    $${PWD}/OAIFolder.h \
    $${PWD}/OAIFolders.h \
    $${PWD}/OAIObjectGroup.h \
    $${PWD}/OAIObjectType.h \
    $${PWD}/OAIUser.h \
# APIs
    $${PWD}/OAIFilesApi.h \
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
    $${PWD}/OAIAssociation.cpp \
    $${PWD}/OAIFileObject.cpp \
    $${PWD}/OAIFiles.cpp \
    $${PWD}/OAIFolder.cpp \
    $${PWD}/OAIFolders.cpp \
    $${PWD}/OAIObjectGroup.cpp \
    $${PWD}/OAIObjectType.cpp \
    $${PWD}/OAIUser.cpp \
# APIs
    $${PWD}/OAIFilesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
