QT += network

HEADERS += \
# Models
    $${PWD}/OAIDirectoryList.h \
    $${PWD}/OAIDirectoryList_items_inner.h \
    $${PWD}/OAIDirectoryList_items_inner_icons.h \
    $${PWD}/OAIJsonSchema.h \
    $${PWD}/OAIJsonSchema_annotations.h \
    $${PWD}/OAIJsonSchema_variant.h \
    $${PWD}/OAIJsonSchema_variant_map_inner.h \
    $${PWD}/OAIRestDescription.h \
    $${PWD}/OAIRestDescription_auth.h \
    $${PWD}/OAIRestDescription_auth_oauth2.h \
    $${PWD}/OAIRestDescription_auth_oauth2_scopes_value.h \
    $${PWD}/OAIRestDescription_endpoints_inner.h \
    $${PWD}/OAIRestMethod.h \
    $${PWD}/OAIRestMethod_mediaUpload.h \
    $${PWD}/OAIRestMethod_mediaUpload_protocols.h \
    $${PWD}/OAIRestMethod_mediaUpload_protocols_resumable.h \
    $${PWD}/OAIRestMethod_mediaUpload_protocols_simple.h \
    $${PWD}/OAIRestMethod_request.h \
    $${PWD}/OAIRestMethod_response.h \
    $${PWD}/OAIRestResource.h \
# APIs
    $${PWD}/OAIApisApi.h \
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
    $${PWD}/OAIDirectoryList.cpp \
    $${PWD}/OAIDirectoryList_items_inner.cpp \
    $${PWD}/OAIDirectoryList_items_inner_icons.cpp \
    $${PWD}/OAIJsonSchema.cpp \
    $${PWD}/OAIJsonSchema_annotations.cpp \
    $${PWD}/OAIJsonSchema_variant.cpp \
    $${PWD}/OAIJsonSchema_variant_map_inner.cpp \
    $${PWD}/OAIRestDescription.cpp \
    $${PWD}/OAIRestDescription_auth.cpp \
    $${PWD}/OAIRestDescription_auth_oauth2.cpp \
    $${PWD}/OAIRestDescription_auth_oauth2_scopes_value.cpp \
    $${PWD}/OAIRestDescription_endpoints_inner.cpp \
    $${PWD}/OAIRestMethod.cpp \
    $${PWD}/OAIRestMethod_mediaUpload.cpp \
    $${PWD}/OAIRestMethod_mediaUpload_protocols.cpp \
    $${PWD}/OAIRestMethod_mediaUpload_protocols_resumable.cpp \
    $${PWD}/OAIRestMethod_mediaUpload_protocols_simple.cpp \
    $${PWD}/OAIRestMethod_request.cpp \
    $${PWD}/OAIRestMethod_response.cpp \
    $${PWD}/OAIRestResource.cpp \
# APIs
    $${PWD}/OAIApisApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
