QT += network

HEADERS += \
# Models
    $${PWD}/OAIListAccountConfigResponse.h \
    $${PWD}/OAIListAccountSecretResponse.h \
    $${PWD}/OAIListAppResponse.h \
    $${PWD}/OAIListAppResponse_meta.h \
    $${PWD}/OAIListDeviceConfigResponse.h \
    $${PWD}/OAIListDeviceResponse.h \
    $${PWD}/OAIListDeviceSecretResponse.h \
    $${PWD}/OAIMicrovisor_v1_account_config.h \
    $${PWD}/OAIMicrovisor_v1_account_secret.h \
    $${PWD}/OAIMicrovisor_v1_app.h \
    $${PWD}/OAIMicrovisor_v1_app_app_manifest.h \
    $${PWD}/OAIMicrovisor_v1_device.h \
    $${PWD}/OAIMicrovisor_v1_device_device_config.h \
    $${PWD}/OAIMicrovisor_v1_device_device_secret.h \
# APIs
    $${PWD}/OAIMicrovisorV1AccountConfigApi.h \
    $${PWD}/OAIMicrovisorV1AccountSecretApi.h \
    $${PWD}/OAIMicrovisorV1AppApi.h \
    $${PWD}/OAIMicrovisorV1AppManifestApi.h \
    $${PWD}/OAIMicrovisorV1DeviceApi.h \
    $${PWD}/OAIMicrovisorV1DeviceConfigApi.h \
    $${PWD}/OAIMicrovisorV1DeviceSecretApi.h \
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
    $${PWD}/OAIListAccountConfigResponse.cpp \
    $${PWD}/OAIListAccountSecretResponse.cpp \
    $${PWD}/OAIListAppResponse.cpp \
    $${PWD}/OAIListAppResponse_meta.cpp \
    $${PWD}/OAIListDeviceConfigResponse.cpp \
    $${PWD}/OAIListDeviceResponse.cpp \
    $${PWD}/OAIListDeviceSecretResponse.cpp \
    $${PWD}/OAIMicrovisor_v1_account_config.cpp \
    $${PWD}/OAIMicrovisor_v1_account_secret.cpp \
    $${PWD}/OAIMicrovisor_v1_app.cpp \
    $${PWD}/OAIMicrovisor_v1_app_app_manifest.cpp \
    $${PWD}/OAIMicrovisor_v1_device.cpp \
    $${PWD}/OAIMicrovisor_v1_device_device_config.cpp \
    $${PWD}/OAIMicrovisor_v1_device_device_secret.cpp \
# APIs
    $${PWD}/OAIMicrovisorV1AccountConfigApi.cpp \
    $${PWD}/OAIMicrovisorV1AccountSecretApi.cpp \
    $${PWD}/OAIMicrovisorV1AppApi.cpp \
    $${PWD}/OAIMicrovisorV1AppManifestApi.cpp \
    $${PWD}/OAIMicrovisorV1DeviceApi.cpp \
    $${PWD}/OAIMicrovisorV1DeviceConfigApi.cpp \
    $${PWD}/OAIMicrovisorV1DeviceSecretApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
