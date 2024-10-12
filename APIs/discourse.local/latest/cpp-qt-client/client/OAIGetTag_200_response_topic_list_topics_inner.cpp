/**
 * Discourse API Documentation
 * This page contains the documentation on how to use Discourse through API calls.  > Note: For any endpoints not listed you can follow the [reverse engineer the Discourse API](https://meta.discourse.org/t/-/20576) guide to figure out how to use an API endpoint.  ### Request Content-Type  The Content-Type for POST and PUT requests can be set to `application/x-www-form-urlencoded`, `multipart/form-data`, or `application/json`.  ### Endpoint Names and Response Content-Type  Most API endpoints provide the same content as their HTML counterparts. For example the URL `/categories` serves a list of categories, the `/categories.json` API provides the same information in JSON format.  Instead of sending API requests to `/categories.json` you may also send them to `/categories` and add an `Accept: application/json` header to the request to get the JSON response. Sending requests with the `Accept` header is necessary if you want to use URLs for related endpoints returned by the API, such as pagination URLs. These URLs are returned without the `.json` prefix so you need to add the header in order to get the correct response format.  ### Authentication  Some endpoints do not require any authentication, pretty much anything else will require you to be authenticated.  To become authenticated you will need to create an API Key from the admin panel.  Once you have your API Key you can pass it in along with your API Username as an HTTP header like this:  ``` curl -X GET \"http://127.0.0.1:3000/admin/users/list/active.json\" \\ -H \"Api-Key: 714552c6148e1617aeab526d0606184b94a80ec048fc09894ff1a72b740c5f19\" \\ -H \"Api-Username: system\" ```  and this is how POST requests will look:  ``` curl -X POST \"http://127.0.0.1:3000/categories\" \\ -H \"Content-Type: multipart/form-data;\" \\ -H \"Api-Key: 714552c6148e1617aeab526d0606184b94a80ec048fc09894ff1a72b740c5f19\" \\ -H \"Api-Username: system\" \\ -F \"name=89853c20-4409-e91a-a8ea-f6cdff96aaaa\" \\ -F \"color=49d9e9\" \\ -F \"text_color=f0fcfd\" ```  ### Boolean values  If an endpoint accepts a boolean be sure to specify it as a lowercase `true` or `false` value unless noted otherwise. 
 *
 * The version of the OpenAPI document: latest
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIGetTag_200_response_topic_list_topics_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetTag_200_response_topic_list_topics_inner::OAIGetTag_200_response_topic_list_topics_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetTag_200_response_topic_list_topics_inner::OAIGetTag_200_response_topic_list_topics_inner() {
    this->initializeModel();
}

OAIGetTag_200_response_topic_list_topics_inner::~OAIGetTag_200_response_topic_list_topics_inner() {}

void OAIGetTag_200_response_topic_list_topics_inner::initializeModel() {

    m_archetype_isSet = false;
    m_archetype_isValid = false;

    m_archived_isSet = false;
    m_archived_isValid = false;

    m_bookmarked_isSet = false;
    m_bookmarked_isValid = false;

    m_bumped_isSet = false;
    m_bumped_isValid = false;

    m_bumped_at_isSet = false;
    m_bumped_at_isValid = false;

    m_category_id_isSet = false;
    m_category_id_isValid = false;

    m_closed_isSet = false;
    m_closed_isValid = false;

    m_created_at_isSet = false;
    m_created_at_isValid = false;

    m_fancy_title_isSet = false;
    m_fancy_title_isValid = false;

    m_featured_link_isSet = false;
    m_featured_link_isValid = false;

    m_has_summary_isSet = false;
    m_has_summary_isValid = false;

    m_highest_post_number_isSet = false;
    m_highest_post_number_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_image_url_isSet = false;
    m_image_url_isValid = false;

    m_last_posted_at_isSet = false;
    m_last_posted_at_isValid = false;

    m_last_poster_username_isSet = false;
    m_last_poster_username_isValid = false;

    m_last_read_post_number_isSet = false;
    m_last_read_post_number_isValid = false;

    m_like_count_isSet = false;
    m_like_count_isValid = false;

    m_liked_isSet = false;
    m_liked_isValid = false;

    m_notification_level_isSet = false;
    m_notification_level_isValid = false;

    m_pinned_isSet = false;
    m_pinned_isValid = false;

    m_pinned_globally_isSet = false;
    m_pinned_globally_isValid = false;

    m_posters_isSet = false;
    m_posters_isValid = false;

    m_posts_count_isSet = false;
    m_posts_count_isValid = false;

    m_reply_count_isSet = false;
    m_reply_count_isValid = false;

    m_slug_isSet = false;
    m_slug_isValid = false;

    m_tags_isSet = false;
    m_tags_isValid = false;

    m_title_isSet = false;
    m_title_isValid = false;

    m_unpinned_isSet = false;
    m_unpinned_isValid = false;

    m_unread_posts_isSet = false;
    m_unread_posts_isValid = false;

    m_unseen_isSet = false;
    m_unseen_isValid = false;

    m_views_isSet = false;
    m_views_isValid = false;

    m_visible_isSet = false;
    m_visible_isValid = false;
}

void OAIGetTag_200_response_topic_list_topics_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetTag_200_response_topic_list_topics_inner::fromJsonObject(QJsonObject json) {

    m_archetype_isValid = ::OpenAPI::fromJsonValue(m_archetype, json[QString("archetype")]);
    m_archetype_isSet = !json[QString("archetype")].isNull() && m_archetype_isValid;

    m_archived_isValid = ::OpenAPI::fromJsonValue(m_archived, json[QString("archived")]);
    m_archived_isSet = !json[QString("archived")].isNull() && m_archived_isValid;

    m_bookmarked_isValid = ::OpenAPI::fromJsonValue(m_bookmarked, json[QString("bookmarked")]);
    m_bookmarked_isSet = !json[QString("bookmarked")].isNull() && m_bookmarked_isValid;

    m_bumped_isValid = ::OpenAPI::fromJsonValue(m_bumped, json[QString("bumped")]);
    m_bumped_isSet = !json[QString("bumped")].isNull() && m_bumped_isValid;

    m_bumped_at_isValid = ::OpenAPI::fromJsonValue(m_bumped_at, json[QString("bumped_at")]);
    m_bumped_at_isSet = !json[QString("bumped_at")].isNull() && m_bumped_at_isValid;

    m_category_id_isValid = ::OpenAPI::fromJsonValue(m_category_id, json[QString("category_id")]);
    m_category_id_isSet = !json[QString("category_id")].isNull() && m_category_id_isValid;

    m_closed_isValid = ::OpenAPI::fromJsonValue(m_closed, json[QString("closed")]);
    m_closed_isSet = !json[QString("closed")].isNull() && m_closed_isValid;

    m_created_at_isValid = ::OpenAPI::fromJsonValue(m_created_at, json[QString("created_at")]);
    m_created_at_isSet = !json[QString("created_at")].isNull() && m_created_at_isValid;

    m_fancy_title_isValid = ::OpenAPI::fromJsonValue(m_fancy_title, json[QString("fancy_title")]);
    m_fancy_title_isSet = !json[QString("fancy_title")].isNull() && m_fancy_title_isValid;

    m_featured_link_isValid = ::OpenAPI::fromJsonValue(m_featured_link, json[QString("featured_link")]);
    m_featured_link_isSet = !json[QString("featured_link")].isNull() && m_featured_link_isValid;

    m_has_summary_isValid = ::OpenAPI::fromJsonValue(m_has_summary, json[QString("has_summary")]);
    m_has_summary_isSet = !json[QString("has_summary")].isNull() && m_has_summary_isValid;

    m_highest_post_number_isValid = ::OpenAPI::fromJsonValue(m_highest_post_number, json[QString("highest_post_number")]);
    m_highest_post_number_isSet = !json[QString("highest_post_number")].isNull() && m_highest_post_number_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_image_url_isValid = ::OpenAPI::fromJsonValue(m_image_url, json[QString("image_url")]);
    m_image_url_isSet = !json[QString("image_url")].isNull() && m_image_url_isValid;

    m_last_posted_at_isValid = ::OpenAPI::fromJsonValue(m_last_posted_at, json[QString("last_posted_at")]);
    m_last_posted_at_isSet = !json[QString("last_posted_at")].isNull() && m_last_posted_at_isValid;

    m_last_poster_username_isValid = ::OpenAPI::fromJsonValue(m_last_poster_username, json[QString("last_poster_username")]);
    m_last_poster_username_isSet = !json[QString("last_poster_username")].isNull() && m_last_poster_username_isValid;

    m_last_read_post_number_isValid = ::OpenAPI::fromJsonValue(m_last_read_post_number, json[QString("last_read_post_number")]);
    m_last_read_post_number_isSet = !json[QString("last_read_post_number")].isNull() && m_last_read_post_number_isValid;

    m_like_count_isValid = ::OpenAPI::fromJsonValue(m_like_count, json[QString("like_count")]);
    m_like_count_isSet = !json[QString("like_count")].isNull() && m_like_count_isValid;

    m_liked_isValid = ::OpenAPI::fromJsonValue(m_liked, json[QString("liked")]);
    m_liked_isSet = !json[QString("liked")].isNull() && m_liked_isValid;

    m_notification_level_isValid = ::OpenAPI::fromJsonValue(m_notification_level, json[QString("notification_level")]);
    m_notification_level_isSet = !json[QString("notification_level")].isNull() && m_notification_level_isValid;

    m_pinned_isValid = ::OpenAPI::fromJsonValue(m_pinned, json[QString("pinned")]);
    m_pinned_isSet = !json[QString("pinned")].isNull() && m_pinned_isValid;

    m_pinned_globally_isValid = ::OpenAPI::fromJsonValue(m_pinned_globally, json[QString("pinned_globally")]);
    m_pinned_globally_isSet = !json[QString("pinned_globally")].isNull() && m_pinned_globally_isValid;

    m_posters_isValid = ::OpenAPI::fromJsonValue(m_posters, json[QString("posters")]);
    m_posters_isSet = !json[QString("posters")].isNull() && m_posters_isValid;

    m_posts_count_isValid = ::OpenAPI::fromJsonValue(m_posts_count, json[QString("posts_count")]);
    m_posts_count_isSet = !json[QString("posts_count")].isNull() && m_posts_count_isValid;

    m_reply_count_isValid = ::OpenAPI::fromJsonValue(m_reply_count, json[QString("reply_count")]);
    m_reply_count_isSet = !json[QString("reply_count")].isNull() && m_reply_count_isValid;

    m_slug_isValid = ::OpenAPI::fromJsonValue(m_slug, json[QString("slug")]);
    m_slug_isSet = !json[QString("slug")].isNull() && m_slug_isValid;

    m_tags_isValid = ::OpenAPI::fromJsonValue(m_tags, json[QString("tags")]);
    m_tags_isSet = !json[QString("tags")].isNull() && m_tags_isValid;

    m_title_isValid = ::OpenAPI::fromJsonValue(m_title, json[QString("title")]);
    m_title_isSet = !json[QString("title")].isNull() && m_title_isValid;

    m_unpinned_isValid = ::OpenAPI::fromJsonValue(m_unpinned, json[QString("unpinned")]);
    m_unpinned_isSet = !json[QString("unpinned")].isNull() && m_unpinned_isValid;

    m_unread_posts_isValid = ::OpenAPI::fromJsonValue(m_unread_posts, json[QString("unread_posts")]);
    m_unread_posts_isSet = !json[QString("unread_posts")].isNull() && m_unread_posts_isValid;

    m_unseen_isValid = ::OpenAPI::fromJsonValue(m_unseen, json[QString("unseen")]);
    m_unseen_isSet = !json[QString("unseen")].isNull() && m_unseen_isValid;

    m_views_isValid = ::OpenAPI::fromJsonValue(m_views, json[QString("views")]);
    m_views_isSet = !json[QString("views")].isNull() && m_views_isValid;

    m_visible_isValid = ::OpenAPI::fromJsonValue(m_visible, json[QString("visible")]);
    m_visible_isSet = !json[QString("visible")].isNull() && m_visible_isValid;
}

QString OAIGetTag_200_response_topic_list_topics_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetTag_200_response_topic_list_topics_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_archetype_isSet) {
        obj.insert(QString("archetype"), ::OpenAPI::toJsonValue(m_archetype));
    }
    if (m_archived_isSet) {
        obj.insert(QString("archived"), ::OpenAPI::toJsonValue(m_archived));
    }
    if (m_bookmarked_isSet) {
        obj.insert(QString("bookmarked"), ::OpenAPI::toJsonValue(m_bookmarked));
    }
    if (m_bumped_isSet) {
        obj.insert(QString("bumped"), ::OpenAPI::toJsonValue(m_bumped));
    }
    if (m_bumped_at_isSet) {
        obj.insert(QString("bumped_at"), ::OpenAPI::toJsonValue(m_bumped_at));
    }
    if (m_category_id_isSet) {
        obj.insert(QString("category_id"), ::OpenAPI::toJsonValue(m_category_id));
    }
    if (m_closed_isSet) {
        obj.insert(QString("closed"), ::OpenAPI::toJsonValue(m_closed));
    }
    if (m_created_at_isSet) {
        obj.insert(QString("created_at"), ::OpenAPI::toJsonValue(m_created_at));
    }
    if (m_fancy_title_isSet) {
        obj.insert(QString("fancy_title"), ::OpenAPI::toJsonValue(m_fancy_title));
    }
    if (m_featured_link_isSet) {
        obj.insert(QString("featured_link"), ::OpenAPI::toJsonValue(m_featured_link));
    }
    if (m_has_summary_isSet) {
        obj.insert(QString("has_summary"), ::OpenAPI::toJsonValue(m_has_summary));
    }
    if (m_highest_post_number_isSet) {
        obj.insert(QString("highest_post_number"), ::OpenAPI::toJsonValue(m_highest_post_number));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_image_url_isSet) {
        obj.insert(QString("image_url"), ::OpenAPI::toJsonValue(m_image_url));
    }
    if (m_last_posted_at_isSet) {
        obj.insert(QString("last_posted_at"), ::OpenAPI::toJsonValue(m_last_posted_at));
    }
    if (m_last_poster_username_isSet) {
        obj.insert(QString("last_poster_username"), ::OpenAPI::toJsonValue(m_last_poster_username));
    }
    if (m_last_read_post_number_isSet) {
        obj.insert(QString("last_read_post_number"), ::OpenAPI::toJsonValue(m_last_read_post_number));
    }
    if (m_like_count_isSet) {
        obj.insert(QString("like_count"), ::OpenAPI::toJsonValue(m_like_count));
    }
    if (m_liked_isSet) {
        obj.insert(QString("liked"), ::OpenAPI::toJsonValue(m_liked));
    }
    if (m_notification_level_isSet) {
        obj.insert(QString("notification_level"), ::OpenAPI::toJsonValue(m_notification_level));
    }
    if (m_pinned_isSet) {
        obj.insert(QString("pinned"), ::OpenAPI::toJsonValue(m_pinned));
    }
    if (m_pinned_globally_isSet) {
        obj.insert(QString("pinned_globally"), ::OpenAPI::toJsonValue(m_pinned_globally));
    }
    if (m_posters.size() > 0) {
        obj.insert(QString("posters"), ::OpenAPI::toJsonValue(m_posters));
    }
    if (m_posts_count_isSet) {
        obj.insert(QString("posts_count"), ::OpenAPI::toJsonValue(m_posts_count));
    }
    if (m_reply_count_isSet) {
        obj.insert(QString("reply_count"), ::OpenAPI::toJsonValue(m_reply_count));
    }
    if (m_slug_isSet) {
        obj.insert(QString("slug"), ::OpenAPI::toJsonValue(m_slug));
    }
    if (m_tags.size() > 0) {
        obj.insert(QString("tags"), ::OpenAPI::toJsonValue(m_tags));
    }
    if (m_title_isSet) {
        obj.insert(QString("title"), ::OpenAPI::toJsonValue(m_title));
    }
    if (m_unpinned_isSet) {
        obj.insert(QString("unpinned"), ::OpenAPI::toJsonValue(m_unpinned));
    }
    if (m_unread_posts_isSet) {
        obj.insert(QString("unread_posts"), ::OpenAPI::toJsonValue(m_unread_posts));
    }
    if (m_unseen_isSet) {
        obj.insert(QString("unseen"), ::OpenAPI::toJsonValue(m_unseen));
    }
    if (m_views_isSet) {
        obj.insert(QString("views"), ::OpenAPI::toJsonValue(m_views));
    }
    if (m_visible_isSet) {
        obj.insert(QString("visible"), ::OpenAPI::toJsonValue(m_visible));
    }
    return obj;
}

QString OAIGetTag_200_response_topic_list_topics_inner::getArchetype() const {
    return m_archetype;
}
void OAIGetTag_200_response_topic_list_topics_inner::setArchetype(const QString &archetype) {
    m_archetype = archetype;
    m_archetype_isSet = true;
}

bool OAIGetTag_200_response_topic_list_topics_inner::is_archetype_Set() const{
    return m_archetype_isSet;
}

bool OAIGetTag_200_response_topic_list_topics_inner::is_archetype_Valid() const{
    return m_archetype_isValid;
}

bool OAIGetTag_200_response_topic_list_topics_inner::isArchived() const {
    return m_archived;
}
void OAIGetTag_200_response_topic_list_topics_inner::setArchived(const bool &archived) {
    m_archived = archived;
    m_archived_isSet = true;
}

bool OAIGetTag_200_response_topic_list_topics_inner::is_archived_Set() const{
    return m_archived_isSet;
}

bool OAIGetTag_200_response_topic_list_topics_inner::is_archived_Valid() const{
    return m_archived_isValid;
}

bool OAIGetTag_200_response_topic_list_topics_inner::isBookmarked() const {
    return m_bookmarked;
}
void OAIGetTag_200_response_topic_list_topics_inner::setBookmarked(const bool &bookmarked) {
    m_bookmarked = bookmarked;
    m_bookmarked_isSet = true;
}

bool OAIGetTag_200_response_topic_list_topics_inner::is_bookmarked_Set() const{
    return m_bookmarked_isSet;
}

bool OAIGetTag_200_response_topic_list_topics_inner::is_bookmarked_Valid() const{
    return m_bookmarked_isValid;
}

bool OAIGetTag_200_response_topic_list_topics_inner::isBumped() const {
    return m_bumped;
}
void OAIGetTag_200_response_topic_list_topics_inner::setBumped(const bool &bumped) {
    m_bumped = bumped;
    m_bumped_isSet = true;
}

bool OAIGetTag_200_response_topic_list_topics_inner::is_bumped_Set() const{
    return m_bumped_isSet;
}

bool OAIGetTag_200_response_topic_list_topics_inner::is_bumped_Valid() const{
    return m_bumped_isValid;
}

QString OAIGetTag_200_response_topic_list_topics_inner::getBumpedAt() const {
    return m_bumped_at;
}
void OAIGetTag_200_response_topic_list_topics_inner::setBumpedAt(const QString &bumped_at) {
    m_bumped_at = bumped_at;
    m_bumped_at_isSet = true;
}

bool OAIGetTag_200_response_topic_list_topics_inner::is_bumped_at_Set() const{
    return m_bumped_at_isSet;
}

bool OAIGetTag_200_response_topic_list_topics_inner::is_bumped_at_Valid() const{
    return m_bumped_at_isValid;
}

qint32 OAIGetTag_200_response_topic_list_topics_inner::getCategoryId() const {
    return m_category_id;
}
void OAIGetTag_200_response_topic_list_topics_inner::setCategoryId(const qint32 &category_id) {
    m_category_id = category_id;
    m_category_id_isSet = true;
}

bool OAIGetTag_200_response_topic_list_topics_inner::is_category_id_Set() const{
    return m_category_id_isSet;
}

bool OAIGetTag_200_response_topic_list_topics_inner::is_category_id_Valid() const{
    return m_category_id_isValid;
}

bool OAIGetTag_200_response_topic_list_topics_inner::isClosed() const {
    return m_closed;
}
void OAIGetTag_200_response_topic_list_topics_inner::setClosed(const bool &closed) {
    m_closed = closed;
    m_closed_isSet = true;
}

bool OAIGetTag_200_response_topic_list_topics_inner::is_closed_Set() const{
    return m_closed_isSet;
}

bool OAIGetTag_200_response_topic_list_topics_inner::is_closed_Valid() const{
    return m_closed_isValid;
}

QString OAIGetTag_200_response_topic_list_topics_inner::getCreatedAt() const {
    return m_created_at;
}
void OAIGetTag_200_response_topic_list_topics_inner::setCreatedAt(const QString &created_at) {
    m_created_at = created_at;
    m_created_at_isSet = true;
}

bool OAIGetTag_200_response_topic_list_topics_inner::is_created_at_Set() const{
    return m_created_at_isSet;
}

bool OAIGetTag_200_response_topic_list_topics_inner::is_created_at_Valid() const{
    return m_created_at_isValid;
}

QString OAIGetTag_200_response_topic_list_topics_inner::getFancyTitle() const {
    return m_fancy_title;
}
void OAIGetTag_200_response_topic_list_topics_inner::setFancyTitle(const QString &fancy_title) {
    m_fancy_title = fancy_title;
    m_fancy_title_isSet = true;
}

bool OAIGetTag_200_response_topic_list_topics_inner::is_fancy_title_Set() const{
    return m_fancy_title_isSet;
}

bool OAIGetTag_200_response_topic_list_topics_inner::is_fancy_title_Valid() const{
    return m_fancy_title_isValid;
}

QString OAIGetTag_200_response_topic_list_topics_inner::getFeaturedLink() const {
    return m_featured_link;
}
void OAIGetTag_200_response_topic_list_topics_inner::setFeaturedLink(const QString &featured_link) {
    m_featured_link = featured_link;
    m_featured_link_isSet = true;
}

bool OAIGetTag_200_response_topic_list_topics_inner::is_featured_link_Set() const{
    return m_featured_link_isSet;
}

bool OAIGetTag_200_response_topic_list_topics_inner::is_featured_link_Valid() const{
    return m_featured_link_isValid;
}

bool OAIGetTag_200_response_topic_list_topics_inner::isHasSummary() const {
    return m_has_summary;
}
void OAIGetTag_200_response_topic_list_topics_inner::setHasSummary(const bool &has_summary) {
    m_has_summary = has_summary;
    m_has_summary_isSet = true;
}

bool OAIGetTag_200_response_topic_list_topics_inner::is_has_summary_Set() const{
    return m_has_summary_isSet;
}

bool OAIGetTag_200_response_topic_list_topics_inner::is_has_summary_Valid() const{
    return m_has_summary_isValid;
}

qint32 OAIGetTag_200_response_topic_list_topics_inner::getHighestPostNumber() const {
    return m_highest_post_number;
}
void OAIGetTag_200_response_topic_list_topics_inner::setHighestPostNumber(const qint32 &highest_post_number) {
    m_highest_post_number = highest_post_number;
    m_highest_post_number_isSet = true;
}

bool OAIGetTag_200_response_topic_list_topics_inner::is_highest_post_number_Set() const{
    return m_highest_post_number_isSet;
}

bool OAIGetTag_200_response_topic_list_topics_inner::is_highest_post_number_Valid() const{
    return m_highest_post_number_isValid;
}

qint32 OAIGetTag_200_response_topic_list_topics_inner::getId() const {
    return m_id;
}
void OAIGetTag_200_response_topic_list_topics_inner::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIGetTag_200_response_topic_list_topics_inner::is_id_Set() const{
    return m_id_isSet;
}

bool OAIGetTag_200_response_topic_list_topics_inner::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIGetTag_200_response_topic_list_topics_inner::getImageUrl() const {
    return m_image_url;
}
void OAIGetTag_200_response_topic_list_topics_inner::setImageUrl(const QString &image_url) {
    m_image_url = image_url;
    m_image_url_isSet = true;
}

bool OAIGetTag_200_response_topic_list_topics_inner::is_image_url_Set() const{
    return m_image_url_isSet;
}

bool OAIGetTag_200_response_topic_list_topics_inner::is_image_url_Valid() const{
    return m_image_url_isValid;
}

QString OAIGetTag_200_response_topic_list_topics_inner::getLastPostedAt() const {
    return m_last_posted_at;
}
void OAIGetTag_200_response_topic_list_topics_inner::setLastPostedAt(const QString &last_posted_at) {
    m_last_posted_at = last_posted_at;
    m_last_posted_at_isSet = true;
}

bool OAIGetTag_200_response_topic_list_topics_inner::is_last_posted_at_Set() const{
    return m_last_posted_at_isSet;
}

bool OAIGetTag_200_response_topic_list_topics_inner::is_last_posted_at_Valid() const{
    return m_last_posted_at_isValid;
}

QString OAIGetTag_200_response_topic_list_topics_inner::getLastPosterUsername() const {
    return m_last_poster_username;
}
void OAIGetTag_200_response_topic_list_topics_inner::setLastPosterUsername(const QString &last_poster_username) {
    m_last_poster_username = last_poster_username;
    m_last_poster_username_isSet = true;
}

bool OAIGetTag_200_response_topic_list_topics_inner::is_last_poster_username_Set() const{
    return m_last_poster_username_isSet;
}

bool OAIGetTag_200_response_topic_list_topics_inner::is_last_poster_username_Valid() const{
    return m_last_poster_username_isValid;
}

qint32 OAIGetTag_200_response_topic_list_topics_inner::getLastReadPostNumber() const {
    return m_last_read_post_number;
}
void OAIGetTag_200_response_topic_list_topics_inner::setLastReadPostNumber(const qint32 &last_read_post_number) {
    m_last_read_post_number = last_read_post_number;
    m_last_read_post_number_isSet = true;
}

bool OAIGetTag_200_response_topic_list_topics_inner::is_last_read_post_number_Set() const{
    return m_last_read_post_number_isSet;
}

bool OAIGetTag_200_response_topic_list_topics_inner::is_last_read_post_number_Valid() const{
    return m_last_read_post_number_isValid;
}

qint32 OAIGetTag_200_response_topic_list_topics_inner::getLikeCount() const {
    return m_like_count;
}
void OAIGetTag_200_response_topic_list_topics_inner::setLikeCount(const qint32 &like_count) {
    m_like_count = like_count;
    m_like_count_isSet = true;
}

bool OAIGetTag_200_response_topic_list_topics_inner::is_like_count_Set() const{
    return m_like_count_isSet;
}

bool OAIGetTag_200_response_topic_list_topics_inner::is_like_count_Valid() const{
    return m_like_count_isValid;
}

bool OAIGetTag_200_response_topic_list_topics_inner::isLiked() const {
    return m_liked;
}
void OAIGetTag_200_response_topic_list_topics_inner::setLiked(const bool &liked) {
    m_liked = liked;
    m_liked_isSet = true;
}

bool OAIGetTag_200_response_topic_list_topics_inner::is_liked_Set() const{
    return m_liked_isSet;
}

bool OAIGetTag_200_response_topic_list_topics_inner::is_liked_Valid() const{
    return m_liked_isValid;
}

qint32 OAIGetTag_200_response_topic_list_topics_inner::getNotificationLevel() const {
    return m_notification_level;
}
void OAIGetTag_200_response_topic_list_topics_inner::setNotificationLevel(const qint32 &notification_level) {
    m_notification_level = notification_level;
    m_notification_level_isSet = true;
}

bool OAIGetTag_200_response_topic_list_topics_inner::is_notification_level_Set() const{
    return m_notification_level_isSet;
}

bool OAIGetTag_200_response_topic_list_topics_inner::is_notification_level_Valid() const{
    return m_notification_level_isValid;
}

bool OAIGetTag_200_response_topic_list_topics_inner::isPinned() const {
    return m_pinned;
}
void OAIGetTag_200_response_topic_list_topics_inner::setPinned(const bool &pinned) {
    m_pinned = pinned;
    m_pinned_isSet = true;
}

bool OAIGetTag_200_response_topic_list_topics_inner::is_pinned_Set() const{
    return m_pinned_isSet;
}

bool OAIGetTag_200_response_topic_list_topics_inner::is_pinned_Valid() const{
    return m_pinned_isValid;
}

bool OAIGetTag_200_response_topic_list_topics_inner::isPinnedGlobally() const {
    return m_pinned_globally;
}
void OAIGetTag_200_response_topic_list_topics_inner::setPinnedGlobally(const bool &pinned_globally) {
    m_pinned_globally = pinned_globally;
    m_pinned_globally_isSet = true;
}

bool OAIGetTag_200_response_topic_list_topics_inner::is_pinned_globally_Set() const{
    return m_pinned_globally_isSet;
}

bool OAIGetTag_200_response_topic_list_topics_inner::is_pinned_globally_Valid() const{
    return m_pinned_globally_isValid;
}

QList<OAIListLatestTopics_200_response_topic_list_topics_inner_posters_inner> OAIGetTag_200_response_topic_list_topics_inner::getPosters() const {
    return m_posters;
}
void OAIGetTag_200_response_topic_list_topics_inner::setPosters(const QList<OAIListLatestTopics_200_response_topic_list_topics_inner_posters_inner> &posters) {
    m_posters = posters;
    m_posters_isSet = true;
}

bool OAIGetTag_200_response_topic_list_topics_inner::is_posters_Set() const{
    return m_posters_isSet;
}

bool OAIGetTag_200_response_topic_list_topics_inner::is_posters_Valid() const{
    return m_posters_isValid;
}

qint32 OAIGetTag_200_response_topic_list_topics_inner::getPostsCount() const {
    return m_posts_count;
}
void OAIGetTag_200_response_topic_list_topics_inner::setPostsCount(const qint32 &posts_count) {
    m_posts_count = posts_count;
    m_posts_count_isSet = true;
}

bool OAIGetTag_200_response_topic_list_topics_inner::is_posts_count_Set() const{
    return m_posts_count_isSet;
}

bool OAIGetTag_200_response_topic_list_topics_inner::is_posts_count_Valid() const{
    return m_posts_count_isValid;
}

qint32 OAIGetTag_200_response_topic_list_topics_inner::getReplyCount() const {
    return m_reply_count;
}
void OAIGetTag_200_response_topic_list_topics_inner::setReplyCount(const qint32 &reply_count) {
    m_reply_count = reply_count;
    m_reply_count_isSet = true;
}

bool OAIGetTag_200_response_topic_list_topics_inner::is_reply_count_Set() const{
    return m_reply_count_isSet;
}

bool OAIGetTag_200_response_topic_list_topics_inner::is_reply_count_Valid() const{
    return m_reply_count_isValid;
}

QString OAIGetTag_200_response_topic_list_topics_inner::getSlug() const {
    return m_slug;
}
void OAIGetTag_200_response_topic_list_topics_inner::setSlug(const QString &slug) {
    m_slug = slug;
    m_slug_isSet = true;
}

bool OAIGetTag_200_response_topic_list_topics_inner::is_slug_Set() const{
    return m_slug_isSet;
}

bool OAIGetTag_200_response_topic_list_topics_inner::is_slug_Valid() const{
    return m_slug_isValid;
}

QList<QJsonValue> OAIGetTag_200_response_topic_list_topics_inner::getTags() const {
    return m_tags;
}
void OAIGetTag_200_response_topic_list_topics_inner::setTags(const QList<QJsonValue> &tags) {
    m_tags = tags;
    m_tags_isSet = true;
}

bool OAIGetTag_200_response_topic_list_topics_inner::is_tags_Set() const{
    return m_tags_isSet;
}

bool OAIGetTag_200_response_topic_list_topics_inner::is_tags_Valid() const{
    return m_tags_isValid;
}

QString OAIGetTag_200_response_topic_list_topics_inner::getTitle() const {
    return m_title;
}
void OAIGetTag_200_response_topic_list_topics_inner::setTitle(const QString &title) {
    m_title = title;
    m_title_isSet = true;
}

bool OAIGetTag_200_response_topic_list_topics_inner::is_title_Set() const{
    return m_title_isSet;
}

bool OAIGetTag_200_response_topic_list_topics_inner::is_title_Valid() const{
    return m_title_isValid;
}

QString OAIGetTag_200_response_topic_list_topics_inner::getUnpinned() const {
    return m_unpinned;
}
void OAIGetTag_200_response_topic_list_topics_inner::setUnpinned(const QString &unpinned) {
    m_unpinned = unpinned;
    m_unpinned_isSet = true;
}

bool OAIGetTag_200_response_topic_list_topics_inner::is_unpinned_Set() const{
    return m_unpinned_isSet;
}

bool OAIGetTag_200_response_topic_list_topics_inner::is_unpinned_Valid() const{
    return m_unpinned_isValid;
}

qint32 OAIGetTag_200_response_topic_list_topics_inner::getUnreadPosts() const {
    return m_unread_posts;
}
void OAIGetTag_200_response_topic_list_topics_inner::setUnreadPosts(const qint32 &unread_posts) {
    m_unread_posts = unread_posts;
    m_unread_posts_isSet = true;
}

bool OAIGetTag_200_response_topic_list_topics_inner::is_unread_posts_Set() const{
    return m_unread_posts_isSet;
}

bool OAIGetTag_200_response_topic_list_topics_inner::is_unread_posts_Valid() const{
    return m_unread_posts_isValid;
}

bool OAIGetTag_200_response_topic_list_topics_inner::isUnseen() const {
    return m_unseen;
}
void OAIGetTag_200_response_topic_list_topics_inner::setUnseen(const bool &unseen) {
    m_unseen = unseen;
    m_unseen_isSet = true;
}

bool OAIGetTag_200_response_topic_list_topics_inner::is_unseen_Set() const{
    return m_unseen_isSet;
}

bool OAIGetTag_200_response_topic_list_topics_inner::is_unseen_Valid() const{
    return m_unseen_isValid;
}

qint32 OAIGetTag_200_response_topic_list_topics_inner::getViews() const {
    return m_views;
}
void OAIGetTag_200_response_topic_list_topics_inner::setViews(const qint32 &views) {
    m_views = views;
    m_views_isSet = true;
}

bool OAIGetTag_200_response_topic_list_topics_inner::is_views_Set() const{
    return m_views_isSet;
}

bool OAIGetTag_200_response_topic_list_topics_inner::is_views_Valid() const{
    return m_views_isValid;
}

bool OAIGetTag_200_response_topic_list_topics_inner::isVisible() const {
    return m_visible;
}
void OAIGetTag_200_response_topic_list_topics_inner::setVisible(const bool &visible) {
    m_visible = visible;
    m_visible_isSet = true;
}

bool OAIGetTag_200_response_topic_list_topics_inner::is_visible_Set() const{
    return m_visible_isSet;
}

bool OAIGetTag_200_response_topic_list_topics_inner::is_visible_Valid() const{
    return m_visible_isValid;
}

bool OAIGetTag_200_response_topic_list_topics_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_archetype_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_archived_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_bookmarked_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_bumped_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_bumped_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_category_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_closed_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_created_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_fancy_title_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_featured_link_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_has_summary_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_highest_post_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_image_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_posted_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_poster_username_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_read_post_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_like_count_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_liked_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_notification_level_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_pinned_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_pinned_globally_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_posters.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_posts_count_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_reply_count_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_slug_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tags.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_title_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_unpinned_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_unread_posts_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_unseen_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_views_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_visible_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGetTag_200_response_topic_list_topics_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
