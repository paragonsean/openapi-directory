QT += network

HEADERS += \
# Models
    $${PWD}/OAIAccountResponse.h \
    $${PWD}/OAIBlendResponse.h \
    $${PWD}/OAIButtonResponse.h \
    $${PWD}/OAIButtonResponseErrorUpscaled.h \
    $${PWD}/OAIDescribeResponse.h \
    $${PWD}/OAIDescribeResponse_embeds_inner.h \
    $${PWD}/OAIDescribeResponse_embeds_inner_image.h \
    $${PWD}/OAIImagineResponse.h \
    $${PWD}/OAIImagineResponseModerated.h \
    $${PWD}/OAIJobCancelResponse.h \
    $${PWD}/OAIJobResponse.h \
    $${PWD}/OAIJobResponse_attachments_inner.h \
    $${PWD}/OAIJobResponse_children_inner.h \
    $${PWD}/OAIResponseError.h \
    $${PWD}/OAIResponseMaxJobs.h \
    $${PWD}/OAI_jobs_blend_post_request.h \
    $${PWD}/OAI_jobs_button_post_request.h \
    $${PWD}/OAI_jobs_describe_post_request.h \
    $${PWD}/OAI_jobs_imagine_post_request.h \
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
    $${PWD}/OAIAccountResponse.cpp \
    $${PWD}/OAIBlendResponse.cpp \
    $${PWD}/OAIButtonResponse.cpp \
    $${PWD}/OAIButtonResponseErrorUpscaled.cpp \
    $${PWD}/OAIDescribeResponse.cpp \
    $${PWD}/OAIDescribeResponse_embeds_inner.cpp \
    $${PWD}/OAIDescribeResponse_embeds_inner_image.cpp \
    $${PWD}/OAIImagineResponse.cpp \
    $${PWD}/OAIImagineResponseModerated.cpp \
    $${PWD}/OAIJobCancelResponse.cpp \
    $${PWD}/OAIJobResponse.cpp \
    $${PWD}/OAIJobResponse_attachments_inner.cpp \
    $${PWD}/OAIJobResponse_children_inner.cpp \
    $${PWD}/OAIResponseError.cpp \
    $${PWD}/OAIResponseMaxJobs.cpp \
    $${PWD}/OAI_jobs_blend_post_request.cpp \
    $${PWD}/OAI_jobs_button_post_request.cpp \
    $${PWD}/OAI_jobs_describe_post_request.cpp \
    $${PWD}/OAI_jobs_imagine_post_request.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
