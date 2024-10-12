QT += network

HEADERS += \
# Models
    $${PWD}/OAIGoogleCloudResourcesettingsV1ListSettingsResponse.h \
    $${PWD}/OAIGoogleCloudResourcesettingsV1Setting.h \
    $${PWD}/OAIGoogleCloudResourcesettingsV1SettingMetadata.h \
    $${PWD}/OAIGoogleCloudResourcesettingsV1Value.h \
    $${PWD}/OAIGoogleCloudResourcesettingsV1ValueEnumValue.h \
    $${PWD}/OAIGoogleCloudResourcesettingsV1ValueStringMap.h \
    $${PWD}/OAIGoogleCloudResourcesettingsV1ValueStringSet.h \
# APIs
    $${PWD}/OAIProjectsApi.h \
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
    $${PWD}/OAIGoogleCloudResourcesettingsV1ListSettingsResponse.cpp \
    $${PWD}/OAIGoogleCloudResourcesettingsV1Setting.cpp \
    $${PWD}/OAIGoogleCloudResourcesettingsV1SettingMetadata.cpp \
    $${PWD}/OAIGoogleCloudResourcesettingsV1Value.cpp \
    $${PWD}/OAIGoogleCloudResourcesettingsV1ValueEnumValue.cpp \
    $${PWD}/OAIGoogleCloudResourcesettingsV1ValueStringMap.cpp \
    $${PWD}/OAIGoogleCloudResourcesettingsV1ValueStringSet.cpp \
# APIs
    $${PWD}/OAIProjectsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
