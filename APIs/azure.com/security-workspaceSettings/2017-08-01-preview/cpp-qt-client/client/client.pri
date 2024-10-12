QT += network

HEADERS += \
# Models
    $${PWD}/OAIWorkspaceSetting.h \
    $${PWD}/OAIWorkspaceSettingList.h \
    $${PWD}/OAIWorkspaceSettingProperties.h \
    $${PWD}/OAIWorkspaceSettings_List_default_response.h \
    $${PWD}/OAIWorkspaceSettings_List_default_response_error.h \
# APIs
    $${PWD}/OAIWorkspaceSettingsApi.h \
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
    $${PWD}/OAIWorkspaceSetting.cpp \
    $${PWD}/OAIWorkspaceSettingList.cpp \
    $${PWD}/OAIWorkspaceSettingProperties.cpp \
    $${PWD}/OAIWorkspaceSettings_List_default_response.cpp \
    $${PWD}/OAIWorkspaceSettings_List_default_response_error.cpp \
# APIs
    $${PWD}/OAIWorkspaceSettingsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
