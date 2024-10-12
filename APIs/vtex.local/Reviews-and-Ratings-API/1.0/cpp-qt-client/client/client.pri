QT += network

HEADERS += \
# Models
    $${PWD}/OAIEditReview_request.h \
    $${PWD}/OAIGetProductRating_200_response.h \
    $${PWD}/OAIGetReviewbyReviewId_200_response.h \
    $${PWD}/OAIGetalistofReviews_200_response.h \
    $${PWD}/OAIGetalistofReviews_200_response_data_inner.h \
    $${PWD}/OAIGetalistofReviews_200_response_range.h \
    $${PWD}/OAISaveMultipleReviewsRequest.h \
    $${PWD}/OAISaveReviewRequest.h \
    $${PWD}/OAISaveReview_200_response.h \
# APIs
    $${PWD}/OAIRatingApi.h \
    $${PWD}/OAIReviewApi.h \
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
    $${PWD}/OAIEditReview_request.cpp \
    $${PWD}/OAIGetProductRating_200_response.cpp \
    $${PWD}/OAIGetReviewbyReviewId_200_response.cpp \
    $${PWD}/OAIGetalistofReviews_200_response.cpp \
    $${PWD}/OAIGetalistofReviews_200_response_data_inner.cpp \
    $${PWD}/OAIGetalistofReviews_200_response_range.cpp \
    $${PWD}/OAISaveMultipleReviewsRequest.cpp \
    $${PWD}/OAISaveReviewRequest.cpp \
    $${PWD}/OAISaveReview_200_response.cpp \
# APIs
    $${PWD}/OAIRatingApi.cpp \
    $${PWD}/OAIReviewApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
