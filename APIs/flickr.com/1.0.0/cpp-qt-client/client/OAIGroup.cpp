/**
 * Flickr API Schema
 * A subset of Flickr's API defined in Swagger format.
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIGroup.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGroup::OAIGroup(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGroup::OAIGroup() {
    this->initializeModel();
}

OAIGroup::~OAIGroup() {}

void OAIGroup::initializeModel() {

    m_blast_isSet = false;
    m_blast_isValid = false;

    m_cover_isSet = false;
    m_cover_isValid = false;

    m_coverphoto_farm_isSet = false;
    m_coverphoto_farm_isValid = false;

    m_coverphoto_server_isSet = false;
    m_coverphoto_server_isValid = false;

    m_coverphoto_url_isSet = false;
    m_coverphoto_url_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_iconfarm_isSet = false;
    m_iconfarm_isValid = false;

    m_iconserver_isSet = false;
    m_iconserver_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_is_admin_isSet = false;
    m_is_admin_isValid = false;

    m_is_member_isSet = false;
    m_is_member_isValid = false;

    m_is_moderator_isSet = false;
    m_is_moderator_isValid = false;

    m_ispoolmoderated_isSet = false;
    m_ispoolmoderated_isValid = false;

    m_lang_isSet = false;
    m_lang_isValid = false;

    m_members_isSet = false;
    m_members_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_path_alias_isSet = false;
    m_path_alias_isValid = false;

    m_pool_count_isSet = false;
    m_pool_count_isValid = false;

    m_pool_rows_isSet = false;
    m_pool_rows_isValid = false;

    m_privacy_isSet = false;
    m_privacy_isValid = false;

    m_restrictions_isSet = false;
    m_restrictions_isValid = false;

    m_roles_isSet = false;
    m_roles_isValid = false;

    m_rules_isSet = false;
    m_rules_isValid = false;

    m_throttle_isSet = false;
    m_throttle_isValid = false;

    m_topic_count_isSet = false;
    m_topic_count_isValid = false;
}

void OAIGroup::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGroup::fromJsonObject(QJsonObject json) {

    m_blast_isValid = ::OpenAPI::fromJsonValue(m_blast, json[QString("blast")]);
    m_blast_isSet = !json[QString("blast")].isNull() && m_blast_isValid;

    m_cover_isValid = ::OpenAPI::fromJsonValue(m_cover, json[QString("cover")]);
    m_cover_isSet = !json[QString("cover")].isNull() && m_cover_isValid;

    m_coverphoto_farm_isValid = ::OpenAPI::fromJsonValue(m_coverphoto_farm, json[QString("coverphoto_farm")]);
    m_coverphoto_farm_isSet = !json[QString("coverphoto_farm")].isNull() && m_coverphoto_farm_isValid;

    m_coverphoto_server_isValid = ::OpenAPI::fromJsonValue(m_coverphoto_server, json[QString("coverphoto_server")]);
    m_coverphoto_server_isSet = !json[QString("coverphoto_server")].isNull() && m_coverphoto_server_isValid;

    m_coverphoto_url_isValid = ::OpenAPI::fromJsonValue(m_coverphoto_url, json[QString("coverphoto_url")]);
    m_coverphoto_url_isSet = !json[QString("coverphoto_url")].isNull() && m_coverphoto_url_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_iconfarm_isValid = ::OpenAPI::fromJsonValue(m_iconfarm, json[QString("iconfarm")]);
    m_iconfarm_isSet = !json[QString("iconfarm")].isNull() && m_iconfarm_isValid;

    m_iconserver_isValid = ::OpenAPI::fromJsonValue(m_iconserver, json[QString("iconserver")]);
    m_iconserver_isSet = !json[QString("iconserver")].isNull() && m_iconserver_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_is_admin_isValid = ::OpenAPI::fromJsonValue(m_is_admin, json[QString("is_admin")]);
    m_is_admin_isSet = !json[QString("is_admin")].isNull() && m_is_admin_isValid;

    m_is_member_isValid = ::OpenAPI::fromJsonValue(m_is_member, json[QString("is_member")]);
    m_is_member_isSet = !json[QString("is_member")].isNull() && m_is_member_isValid;

    m_is_moderator_isValid = ::OpenAPI::fromJsonValue(m_is_moderator, json[QString("is_moderator")]);
    m_is_moderator_isSet = !json[QString("is_moderator")].isNull() && m_is_moderator_isValid;

    m_ispoolmoderated_isValid = ::OpenAPI::fromJsonValue(m_ispoolmoderated, json[QString("ispoolmoderated")]);
    m_ispoolmoderated_isSet = !json[QString("ispoolmoderated")].isNull() && m_ispoolmoderated_isValid;

    m_lang_isValid = ::OpenAPI::fromJsonValue(m_lang, json[QString("lang")]);
    m_lang_isSet = !json[QString("lang")].isNull() && m_lang_isValid;

    m_members_isValid = ::OpenAPI::fromJsonValue(m_members, json[QString("members")]);
    m_members_isSet = !json[QString("members")].isNull() && m_members_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_path_alias_isValid = ::OpenAPI::fromJsonValue(m_path_alias, json[QString("path_alias")]);
    m_path_alias_isSet = !json[QString("path_alias")].isNull() && m_path_alias_isValid;

    m_pool_count_isValid = ::OpenAPI::fromJsonValue(m_pool_count, json[QString("pool_count")]);
    m_pool_count_isSet = !json[QString("pool_count")].isNull() && m_pool_count_isValid;

    m_pool_rows_isValid = ::OpenAPI::fromJsonValue(m_pool_rows, json[QString("pool_rows")]);
    m_pool_rows_isSet = !json[QString("pool_rows")].isNull() && m_pool_rows_isValid;

    m_privacy_isValid = ::OpenAPI::fromJsonValue(m_privacy, json[QString("privacy")]);
    m_privacy_isSet = !json[QString("privacy")].isNull() && m_privacy_isValid;

    m_restrictions_isValid = ::OpenAPI::fromJsonValue(m_restrictions, json[QString("restrictions")]);
    m_restrictions_isSet = !json[QString("restrictions")].isNull() && m_restrictions_isValid;

    m_roles_isValid = ::OpenAPI::fromJsonValue(m_roles, json[QString("roles")]);
    m_roles_isSet = !json[QString("roles")].isNull() && m_roles_isValid;

    m_rules_isValid = ::OpenAPI::fromJsonValue(m_rules, json[QString("rules")]);
    m_rules_isSet = !json[QString("rules")].isNull() && m_rules_isValid;

    m_throttle_isValid = ::OpenAPI::fromJsonValue(m_throttle, json[QString("throttle")]);
    m_throttle_isSet = !json[QString("throttle")].isNull() && m_throttle_isValid;

    m_topic_count_isValid = ::OpenAPI::fromJsonValue(m_topic_count, json[QString("topic_count")]);
    m_topic_count_isSet = !json[QString("topic_count")].isNull() && m_topic_count_isValid;
}

QString OAIGroup::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGroup::asJsonObject() const {
    QJsonObject obj;
    if (m_blast.isSet()) {
        obj.insert(QString("blast"), ::OpenAPI::toJsonValue(m_blast));
    }
    if (m_cover.isSet()) {
        obj.insert(QString("cover"), ::OpenAPI::toJsonValue(m_cover));
    }
    if (m_coverphoto_farm_isSet) {
        obj.insert(QString("coverphoto_farm"), ::OpenAPI::toJsonValue(m_coverphoto_farm));
    }
    if (m_coverphoto_server_isSet) {
        obj.insert(QString("coverphoto_server"), ::OpenAPI::toJsonValue(m_coverphoto_server));
    }
    if (m_coverphoto_url.isSet()) {
        obj.insert(QString("coverphoto_url"), ::OpenAPI::toJsonValue(m_coverphoto_url));
    }
    if (m_description.isSet()) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_iconfarm_isSet) {
        obj.insert(QString("iconfarm"), ::OpenAPI::toJsonValue(m_iconfarm));
    }
    if (m_iconserver_isSet) {
        obj.insert(QString("iconserver"), ::OpenAPI::toJsonValue(m_iconserver));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_is_admin_isSet) {
        obj.insert(QString("is_admin"), ::OpenAPI::toJsonValue(m_is_admin));
    }
    if (m_is_member_isSet) {
        obj.insert(QString("is_member"), ::OpenAPI::toJsonValue(m_is_member));
    }
    if (m_is_moderator_isSet) {
        obj.insert(QString("is_moderator"), ::OpenAPI::toJsonValue(m_is_moderator));
    }
    if (m_ispoolmoderated_isSet) {
        obj.insert(QString("ispoolmoderated"), ::OpenAPI::toJsonValue(m_ispoolmoderated));
    }
    if (m_lang_isSet) {
        obj.insert(QString("lang"), ::OpenAPI::toJsonValue(m_lang));
    }
    if (m_members.isSet()) {
        obj.insert(QString("members"), ::OpenAPI::toJsonValue(m_members));
    }
    if (m_name.isSet()) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_path_alias_isSet) {
        obj.insert(QString("path_alias"), ::OpenAPI::toJsonValue(m_path_alias));
    }
    if (m_pool_count.isSet()) {
        obj.insert(QString("pool_count"), ::OpenAPI::toJsonValue(m_pool_count));
    }
    if (m_pool_rows_isSet) {
        obj.insert(QString("pool_rows"), ::OpenAPI::toJsonValue(m_pool_rows));
    }
    if (m_privacy.isSet()) {
        obj.insert(QString("privacy"), ::OpenAPI::toJsonValue(m_privacy));
    }
    if (m_restrictions.isSet()) {
        obj.insert(QString("restrictions"), ::OpenAPI::toJsonValue(m_restrictions));
    }
    if (m_roles.isSet()) {
        obj.insert(QString("roles"), ::OpenAPI::toJsonValue(m_roles));
    }
    if (m_rules.isSet()) {
        obj.insert(QString("rules"), ::OpenAPI::toJsonValue(m_rules));
    }
    if (m_throttle.isSet()) {
        obj.insert(QString("throttle"), ::OpenAPI::toJsonValue(m_throttle));
    }
    if (m_topic_count.isSet()) {
        obj.insert(QString("topic_count"), ::OpenAPI::toJsonValue(m_topic_count));
    }
    return obj;
}

OAIGroup_blast OAIGroup::getBlast() const {
    return m_blast;
}
void OAIGroup::setBlast(const OAIGroup_blast &blast) {
    m_blast = blast;
    m_blast_isSet = true;
}

bool OAIGroup::is_blast_Set() const{
    return m_blast_isSet;
}

bool OAIGroup::is_blast_Valid() const{
    return m_blast_isValid;
}

OAICover OAIGroup::getCover() const {
    return m_cover;
}
void OAIGroup::setCover(const OAICover &cover) {
    m_cover = cover;
    m_cover_isSet = true;
}

bool OAIGroup::is_cover_Set() const{
    return m_cover_isSet;
}

bool OAIGroup::is_cover_Valid() const{
    return m_cover_isValid;
}

QString OAIGroup::getCoverphotoFarm() const {
    return m_coverphoto_farm;
}
void OAIGroup::setCoverphotoFarm(const QString &coverphoto_farm) {
    m_coverphoto_farm = coverphoto_farm;
    m_coverphoto_farm_isSet = true;
}

bool OAIGroup::is_coverphoto_farm_Set() const{
    return m_coverphoto_farm_isSet;
}

bool OAIGroup::is_coverphoto_farm_Valid() const{
    return m_coverphoto_farm_isValid;
}

QString OAIGroup::getCoverphotoServer() const {
    return m_coverphoto_server;
}
void OAIGroup::setCoverphotoServer(const QString &coverphoto_server) {
    m_coverphoto_server = coverphoto_server;
    m_coverphoto_server_isSet = true;
}

bool OAIGroup::is_coverphoto_server_Set() const{
    return m_coverphoto_server_isSet;
}

bool OAIGroup::is_coverphoto_server_Valid() const{
    return m_coverphoto_server_isValid;
}

OAIPhotoURLs OAIGroup::getCoverphotoUrl() const {
    return m_coverphoto_url;
}
void OAIGroup::setCoverphotoUrl(const OAIPhotoURLs &coverphoto_url) {
    m_coverphoto_url = coverphoto_url;
    m_coverphoto_url_isSet = true;
}

bool OAIGroup::is_coverphoto_url_Set() const{
    return m_coverphoto_url_isSet;
}

bool OAIGroup::is_coverphoto_url_Valid() const{
    return m_coverphoto_url_isValid;
}

OAIGetFavoritesContextByID_200_response_count OAIGroup::getDescription() const {
    return m_description;
}
void OAIGroup::setDescription(const OAIGetFavoritesContextByID_200_response_count &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIGroup::is_description_Set() const{
    return m_description_isSet;
}

bool OAIGroup::is_description_Valid() const{
    return m_description_isValid;
}

QString OAIGroup::getIconfarm() const {
    return m_iconfarm;
}
void OAIGroup::setIconfarm(const QString &iconfarm) {
    m_iconfarm = iconfarm;
    m_iconfarm_isSet = true;
}

bool OAIGroup::is_iconfarm_Set() const{
    return m_iconfarm_isSet;
}

bool OAIGroup::is_iconfarm_Valid() const{
    return m_iconfarm_isValid;
}

QString OAIGroup::getIconserver() const {
    return m_iconserver;
}
void OAIGroup::setIconserver(const QString &iconserver) {
    m_iconserver = iconserver;
    m_iconserver_isSet = true;
}

bool OAIGroup::is_iconserver_Set() const{
    return m_iconserver_isSet;
}

bool OAIGroup::is_iconserver_Valid() const{
    return m_iconserver_isValid;
}

QString OAIGroup::getId() const {
    return m_id;
}
void OAIGroup::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIGroup::is_id_Set() const{
    return m_id_isSet;
}

bool OAIGroup::is_id_Valid() const{
    return m_id_isValid;
}

bool OAIGroup::isIsAdmin() const {
    return m_is_admin;
}
void OAIGroup::setIsAdmin(const bool &is_admin) {
    m_is_admin = is_admin;
    m_is_admin_isSet = true;
}

bool OAIGroup::is_is_admin_Set() const{
    return m_is_admin_isSet;
}

bool OAIGroup::is_is_admin_Valid() const{
    return m_is_admin_isValid;
}

bool OAIGroup::isIsMember() const {
    return m_is_member;
}
void OAIGroup::setIsMember(const bool &is_member) {
    m_is_member = is_member;
    m_is_member_isSet = true;
}

bool OAIGroup::is_is_member_Set() const{
    return m_is_member_isSet;
}

bool OAIGroup::is_is_member_Valid() const{
    return m_is_member_isValid;
}

bool OAIGroup::isIsModerator() const {
    return m_is_moderator;
}
void OAIGroup::setIsModerator(const bool &is_moderator) {
    m_is_moderator = is_moderator;
    m_is_moderator_isSet = true;
}

bool OAIGroup::is_is_moderator_Set() const{
    return m_is_moderator_isSet;
}

bool OAIGroup::is_is_moderator_Valid() const{
    return m_is_moderator_isValid;
}

bool OAIGroup::isIspoolmoderated() const {
    return m_ispoolmoderated;
}
void OAIGroup::setIspoolmoderated(const bool &ispoolmoderated) {
    m_ispoolmoderated = ispoolmoderated;
    m_ispoolmoderated_isSet = true;
}

bool OAIGroup::is_ispoolmoderated_Set() const{
    return m_ispoolmoderated_isSet;
}

bool OAIGroup::is_ispoolmoderated_Valid() const{
    return m_ispoolmoderated_isValid;
}

QString OAIGroup::getLang() const {
    return m_lang;
}
void OAIGroup::setLang(const QString &lang) {
    m_lang = lang;
    m_lang_isSet = true;
}

bool OAIGroup::is_lang_Set() const{
    return m_lang_isSet;
}

bool OAIGroup::is_lang_Valid() const{
    return m_lang_isValid;
}

OAIGetFavoritesContextByID_200_response_count OAIGroup::getMembers() const {
    return m_members;
}
void OAIGroup::setMembers(const OAIGetFavoritesContextByID_200_response_count &members) {
    m_members = members;
    m_members_isSet = true;
}

bool OAIGroup::is_members_Set() const{
    return m_members_isSet;
}

bool OAIGroup::is_members_Valid() const{
    return m_members_isValid;
}

OAIGetFavoritesContextByID_200_response_count OAIGroup::getName() const {
    return m_name;
}
void OAIGroup::setName(const OAIGetFavoritesContextByID_200_response_count &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIGroup::is_name_Set() const{
    return m_name_isSet;
}

bool OAIGroup::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIGroup::getPathAlias() const {
    return m_path_alias;
}
void OAIGroup::setPathAlias(const QString &path_alias) {
    m_path_alias = path_alias;
    m_path_alias_isSet = true;
}

bool OAIGroup::is_path_alias_Set() const{
    return m_path_alias_isSet;
}

bool OAIGroup::is_path_alias_Valid() const{
    return m_path_alias_isValid;
}

OAIGetFavoritesContextByID_200_response_count OAIGroup::getPoolCount() const {
    return m_pool_count;
}
void OAIGroup::setPoolCount(const OAIGetFavoritesContextByID_200_response_count &pool_count) {
    m_pool_count = pool_count;
    m_pool_count_isSet = true;
}

bool OAIGroup::is_pool_count_Set() const{
    return m_pool_count_isSet;
}

bool OAIGroup::is_pool_count_Valid() const{
    return m_pool_count_isValid;
}

qint32 OAIGroup::getPoolRows() const {
    return m_pool_rows;
}
void OAIGroup::setPoolRows(const qint32 &pool_rows) {
    m_pool_rows = pool_rows;
    m_pool_rows_isSet = true;
}

bool OAIGroup::is_pool_rows_Set() const{
    return m_pool_rows_isSet;
}

bool OAIGroup::is_pool_rows_Valid() const{
    return m_pool_rows_isValid;
}

OAIGetFavoritesContextByID_200_response_count OAIGroup::getPrivacy() const {
    return m_privacy;
}
void OAIGroup::setPrivacy(const OAIGetFavoritesContextByID_200_response_count &privacy) {
    m_privacy = privacy;
    m_privacy_isSet = true;
}

bool OAIGroup::is_privacy_Set() const{
    return m_privacy_isSet;
}

bool OAIGroup::is_privacy_Valid() const{
    return m_privacy_isValid;
}

OAIGroup_restrictions OAIGroup::getRestrictions() const {
    return m_restrictions;
}
void OAIGroup::setRestrictions(const OAIGroup_restrictions &restrictions) {
    m_restrictions = restrictions;
    m_restrictions_isSet = true;
}

bool OAIGroup::is_restrictions_Set() const{
    return m_restrictions_isSet;
}

bool OAIGroup::is_restrictions_Valid() const{
    return m_restrictions_isValid;
}

OAIGroup_roles OAIGroup::getRoles() const {
    return m_roles;
}
void OAIGroup::setRoles(const OAIGroup_roles &roles) {
    m_roles = roles;
    m_roles_isSet = true;
}

bool OAIGroup::is_roles_Set() const{
    return m_roles_isSet;
}

bool OAIGroup::is_roles_Valid() const{
    return m_roles_isValid;
}

OAIGetFavoritesContextByID_200_response_count OAIGroup::getRules() const {
    return m_rules;
}
void OAIGroup::setRules(const OAIGetFavoritesContextByID_200_response_count &rules) {
    m_rules = rules;
    m_rules_isSet = true;
}

bool OAIGroup::is_rules_Set() const{
    return m_rules_isSet;
}

bool OAIGroup::is_rules_Valid() const{
    return m_rules_isValid;
}

OAIGroup_throttle OAIGroup::getThrottle() const {
    return m_throttle;
}
void OAIGroup::setThrottle(const OAIGroup_throttle &throttle) {
    m_throttle = throttle;
    m_throttle_isSet = true;
}

bool OAIGroup::is_throttle_Set() const{
    return m_throttle_isSet;
}

bool OAIGroup::is_throttle_Valid() const{
    return m_throttle_isValid;
}

OAIGetFavoritesContextByID_200_response_count OAIGroup::getTopicCount() const {
    return m_topic_count;
}
void OAIGroup::setTopicCount(const OAIGetFavoritesContextByID_200_response_count &topic_count) {
    m_topic_count = topic_count;
    m_topic_count_isSet = true;
}

bool OAIGroup::is_topic_count_Set() const{
    return m_topic_count_isSet;
}

bool OAIGroup::is_topic_count_Valid() const{
    return m_topic_count_isValid;
}

bool OAIGroup::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_blast.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_cover.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_coverphoto_farm_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_coverphoto_server_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_coverphoto_url.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_description.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_iconfarm_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_iconserver_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_admin_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_member_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_moderator_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ispoolmoderated_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_lang_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_members.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_name.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_path_alias_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_pool_count.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_pool_rows_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_privacy.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_restrictions.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_roles.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_rules.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_throttle.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_topic_count.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGroup::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
