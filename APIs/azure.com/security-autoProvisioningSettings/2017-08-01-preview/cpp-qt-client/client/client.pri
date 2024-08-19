QT += network

HEADERS += \
# Models
    $${PWD}/OAIAutoProvisioningSetting.h \
    $${PWD}/OAIAutoProvisioningSettingList.h \
    $${PWD}/OAIAutoProvisioningSettingProperties.h \
    $${PWD}/OAIAutoProvisioningSettings_List_default_response.h \
    $${PWD}/OAIAutoProvisioningSettings_List_default_response_error.h \
# APIs
    $${PWD}/OAIAutoProvisioningSettingsApi.h \
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
    $${PWD}/OAIAutoProvisioningSetting.cpp \
    $${PWD}/OAIAutoProvisioningSettingList.cpp \
    $${PWD}/OAIAutoProvisioningSettingProperties.cpp \
    $${PWD}/OAIAutoProvisioningSettings_List_default_response.cpp \
    $${PWD}/OAIAutoProvisioningSettings_List_default_response_error.cpp \
# APIs
    $${PWD}/OAIAutoProvisioningSettingsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
