QT += network

HEADERS += \
# Models
    $${PWD}/OAIAttachment.h \
    $${PWD}/OAIBatchCreatePermissionsRequest.h \
    $${PWD}/OAIBatchCreatePermissionsResponse.h \
    $${PWD}/OAIBatchDeletePermissionsRequest.h \
    $${PWD}/OAICreatePermissionRequest.h \
    $${PWD}/OAIGroup.h \
    $${PWD}/OAIListContent.h \
    $${PWD}/OAIListItem.h \
    $${PWD}/OAIListNotesResponse.h \
    $${PWD}/OAINote.h \
    $${PWD}/OAIPermission.h \
    $${PWD}/OAISection.h \
    $${PWD}/OAITextContent.h \
    $${PWD}/OAIUser.h \
# APIs
    $${PWD}/OAINotesApi.h \
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
    $${PWD}/OAIAttachment.cpp \
    $${PWD}/OAIBatchCreatePermissionsRequest.cpp \
    $${PWD}/OAIBatchCreatePermissionsResponse.cpp \
    $${PWD}/OAIBatchDeletePermissionsRequest.cpp \
    $${PWD}/OAICreatePermissionRequest.cpp \
    $${PWD}/OAIGroup.cpp \
    $${PWD}/OAIListContent.cpp \
    $${PWD}/OAIListItem.cpp \
    $${PWD}/OAIListNotesResponse.cpp \
    $${PWD}/OAINote.cpp \
    $${PWD}/OAIPermission.cpp \
    $${PWD}/OAISection.cpp \
    $${PWD}/OAITextContent.cpp \
    $${PWD}/OAIUser.cpp \
# APIs
    $${PWD}/OAINotesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
