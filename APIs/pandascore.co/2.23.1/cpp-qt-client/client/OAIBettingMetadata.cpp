/**
 * PandaScore REST API for All Videogames
 *  # Introduction  Whether you're looking to build an official Pandascore integration for your service, or you just want to build something awesome, [we can help you get started](/home).  The API works over the HTTPS protocol, and is accessed from the `api.pandascore.co` domain.  - The current endpoint is [https://api.pandascore.co](https://api.pandascore.co). - All data is sent and received as JSON by default. - Blank fields are included with `null` values instead of being omitted. - All timestamps are returned in ISO-8601 format  ### About this documentation  Clicking on a query parameter like `filter` or `search` will show you the available options: ![filter](/doc/images/query_param_details.jpg)  You can also click on a response to see the detailed response schema: ![response](/doc/images/response_schema.jpg)  ## Events hierarchy  The PandaScore API allows you to access data about eSports events by using a certain structure detailed below.  **Leagues**  Leagues are the top level events. They don't have a date and represent a regular competition. A League is composed of one or several series.   Some League of Legends leagues are: _EU LCS, NA LCS, LCK, etc._   Some Dota 2 leagues are: _ESL One, GESC, The International, PGL, etc._  **Series**  A Serie represents an occurrence of a league event.   The EU LCS league has two series per year: _spring 2017, summer 2017, spring 2016, summer 2016 etc._   Some Dota2 Series examples would be: _Changsha Major, Open Bucharest, Frankfurt, i-League Invitational etc._  **Tournaments**  Tournaments groups all the matches of a serie under \"stages\" and \"groups\".   The tournaments of the EU LCS of summer 2017 are: _Group A, Group B, Playoffs, etc._   Some Dota 2 tournaments are: _Group A, Group B, Playoffs, etc._  **Matches**  Finally we have matches which have two players or teams (depending on the played videogame) and several games (the rounds of the match).   Matches of the group A in the EU LCS of summer 2017 are: _G2 vs FNC, MSF vs NIP, etc._   Matches of the group A in the ESL One, Genting tournamnet are: _Lower Round 1, Quarterfinal, Upper Final, etc._    **Please note that some matches may be listed as \"TBD vs TBD\" if the matchup is not announced yet, for example the date of the Final match is known but the quarterfinal is still being played.**   ![Structure](/doc/images/structure.png)  ## Formats  &lt;!-- The API currently supports the JSON format by default, as well as the XML format. Add the desired extension to your request URL in order to get that format. --&gt; The API currently supports the JSON format by default.  Other formats may be added depending on user needs.  ## Pagination  The Pandascore API paginates all resources on the index method.  Requests that return multiple items will be paginated to 50 items by default. You can specify further pages with the `page[number]` parameter. You can also set a custom page size (up to 100) with the `page[size]` parameter.  The `Link` HTTP response header contains pagination data with `first`, `previous`, `next` and `last` raw page links when available, under the format  ``` Link: &lt;https://api.pandascore.co/{Resource}?page=X+1&gt;; rel=\"next\", &lt;https://api.pandascore.co/{Resource}?page=X-1&gt;; rel=\"prev\", &lt;https://api.pandascore.co/{Resource}?page=1&gt;; rel=\"first\", &lt;https://api.pandascore.co/{Resource}?page=X+n&gt;; rel=\"last\" ```  There is also:  * A `X-Page` header field, which contains the current page. * A `X-Per-Page` header field, which contains the current pagination length. * A `X-Total` header field, which contains the total count of items across all pages.  ## Filtering  The `filter` query parameter can be used to filter a collection by one or several fields for one or several values. The `filter` parameter takes the field to filter as a key, and the values to filter as the value. Multiples values must be comma-separated (`,`).  For example, the following is a request for all the champions with a name matching Twitch or Brand exactly, but only with 21 armor:  ``` GET /lol/champions?filter[name]=Brand,Twitch&amp;filter[armor]=21&amp;token=YOUR_ACCESS_TOKEN ```  ## Range  The `range` parameter is a hash that allows filtering fields by an interval. Only values between the given two comma-separated bounds will be returned. The bounds are inclusive.  For example, the following is a request for all the champions with `hp` within 500 and 1000:  ``` GET /lol/champions?range[hp]=500,1000&amp;token=YOUR_ACCESS_TOKEN ```  ## Search  The `search` parameter is a bit like the `filter` parameter, but it will return all results where the values **contain** the given parameter.  Note: this only works on strings. Searching with integer values is not supported and `filter` or `range` parameters may be better suited for your needs here.  For example, to get all the champions with a name containing `\"twi\"`:  ``` $ curl -sg -H 'Authorization: Bearer YOUR_ACCESS_TOKEN' 'https://api.pandascore.co/lol/champions?search[name]=twi' | jq -S '.[].name' \"Twitch\" \"Twisted Fate\" ```  ## Sorting  All index endpoints support multiple sort fields with comma-separation (`,`); the fields are applied in the order specified.  The sort order for each field is ascending unless it is prefixed with a minus (U+002D HYPHEN-MINUS, “-“), in which case it is descending.  For example, `GET /lol/champions?sort=attackdamage,-name&amp;token=YOUR_ACCESS_TOKEN` will return all the champions sorted by attack damage. Any champions with the same attack damage will then be sorted by their names in descending alphabetical order.  ## Rate limiting  Depending on your current plan, you will have a different rate limit. Your plan and your current request count [are available on your dashboard](https://pandascore.co/settings).  With the **free plan**, you have a limit of 1000 requests per hour, others plans have a limit of 4000 requests per hour. The number of remaining requests is available in the `X-Rate-Limit-Remaining` response header.  Your API key is included in all the examples on this page, so you can test any example right away. **Only you can see this value.**  # Authentication  The authentication on the Pandascore API works with access tokens.  All developers need to [create an account](https://pandascore.co/users/sign_in) before getting started, in order to get an access token. The access token should not be shared.  **Your token can be found and regenerated from [your dashboard](https://pandascore.co/settings).**  The access token can be passed in the URL with the `token` query string parameter, or in the `Authorization: Bearer` header field.  &lt;!-- ReDoc-Inject: &lt;security-definitions&gt; --&gt; 
 *
 * The version of the OpenAPI document: 2.23.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIBettingMetadata.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIBettingMetadata::OAIBettingMetadata(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIBettingMetadata::OAIBettingMetadata() {
    this->initializeModel();
}

OAIBettingMetadata::~OAIBettingMetadata() {}

void OAIBettingMetadata::initializeModel() {

    m_betting_group_isSet = false;
    m_betting_group_isValid = false;

    m_blueprint_isSet = false;
    m_blueprint_isValid = false;

    m_bookable_isSet = false;
    m_bookable_isValid = false;

    m_booked_isSet = false;
    m_booked_isValid = false;

    m_live_available_isSet = false;
    m_live_available_isValid = false;

    m_markets_created_isSet = false;
    m_markets_created_isValid = false;

    m_markets_updated_at_isSet = false;
    m_markets_updated_at_isValid = false;

    m_pandascore_reviewed_isSet = false;
    m_pandascore_reviewed_isValid = false;

    m_settled_isSet = false;
    m_settled_isValid = false;
}

void OAIBettingMetadata::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIBettingMetadata::fromJsonObject(QJsonObject json) {

    m_betting_group_isValid = ::OpenAPI::fromJsonValue(m_betting_group, json[QString("betting_group")]);
    m_betting_group_isSet = !json[QString("betting_group")].isNull() && m_betting_group_isValid;

    m_blueprint_isValid = ::OpenAPI::fromJsonValue(m_blueprint, json[QString("blueprint")]);
    m_blueprint_isSet = !json[QString("blueprint")].isNull() && m_blueprint_isValid;

    m_bookable_isValid = ::OpenAPI::fromJsonValue(m_bookable, json[QString("bookable")]);
    m_bookable_isSet = !json[QString("bookable")].isNull() && m_bookable_isValid;

    m_booked_isValid = ::OpenAPI::fromJsonValue(m_booked, json[QString("booked")]);
    m_booked_isSet = !json[QString("booked")].isNull() && m_booked_isValid;

    m_live_available_isValid = ::OpenAPI::fromJsonValue(m_live_available, json[QString("live_available")]);
    m_live_available_isSet = !json[QString("live_available")].isNull() && m_live_available_isValid;

    m_markets_created_isValid = ::OpenAPI::fromJsonValue(m_markets_created, json[QString("markets_created")]);
    m_markets_created_isSet = !json[QString("markets_created")].isNull() && m_markets_created_isValid;

    m_markets_updated_at_isValid = ::OpenAPI::fromJsonValue(m_markets_updated_at, json[QString("markets_updated_at")]);
    m_markets_updated_at_isSet = !json[QString("markets_updated_at")].isNull() && m_markets_updated_at_isValid;

    m_pandascore_reviewed_isValid = ::OpenAPI::fromJsonValue(m_pandascore_reviewed, json[QString("pandascore_reviewed")]);
    m_pandascore_reviewed_isSet = !json[QString("pandascore_reviewed")].isNull() && m_pandascore_reviewed_isValid;

    m_settled_isValid = ::OpenAPI::fromJsonValue(m_settled, json[QString("settled")]);
    m_settled_isSet = !json[QString("settled")].isNull() && m_settled_isValid;
}

QString OAIBettingMetadata::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIBettingMetadata::asJsonObject() const {
    QJsonObject obj;
    if (m_betting_group.isSet()) {
        obj.insert(QString("betting_group"), ::OpenAPI::toJsonValue(m_betting_group));
    }
    if (m_blueprint.isSet()) {
        obj.insert(QString("blueprint"), ::OpenAPI::toJsonValue(m_blueprint));
    }
    if (m_bookable_isSet) {
        obj.insert(QString("bookable"), ::OpenAPI::toJsonValue(m_bookable));
    }
    if (m_booked_isSet) {
        obj.insert(QString("booked"), ::OpenAPI::toJsonValue(m_booked));
    }
    if (m_live_available_isSet) {
        obj.insert(QString("live_available"), ::OpenAPI::toJsonValue(m_live_available));
    }
    if (m_markets_created_isSet) {
        obj.insert(QString("markets_created"), ::OpenAPI::toJsonValue(m_markets_created));
    }
    if (m_markets_updated_at_isSet) {
        obj.insert(QString("markets_updated_at"), ::OpenAPI::toJsonValue(m_markets_updated_at));
    }
    if (m_pandascore_reviewed_isSet) {
        obj.insert(QString("pandascore_reviewed"), ::OpenAPI::toJsonValue(m_pandascore_reviewed));
    }
    if (m_settled_isSet) {
        obj.insert(QString("settled"), ::OpenAPI::toJsonValue(m_settled));
    }
    return obj;
}

OAIBettingGroup_1 OAIBettingMetadata::getBettingGroup() const {
    return m_betting_group;
}
void OAIBettingMetadata::setBettingGroup(const OAIBettingGroup_1 &betting_group) {
    m_betting_group = betting_group;
    m_betting_group_isSet = true;
}

bool OAIBettingMetadata::is_betting_group_Set() const{
    return m_betting_group_isSet;
}

bool OAIBettingMetadata::is_betting_group_Valid() const{
    return m_betting_group_isValid;
}

OAIBlueprint_1 OAIBettingMetadata::getBlueprint() const {
    return m_blueprint;
}
void OAIBettingMetadata::setBlueprint(const OAIBlueprint_1 &blueprint) {
    m_blueprint = blueprint;
    m_blueprint_isSet = true;
}

bool OAIBettingMetadata::is_blueprint_Set() const{
    return m_blueprint_isSet;
}

bool OAIBettingMetadata::is_blueprint_Valid() const{
    return m_blueprint_isValid;
}

bool OAIBettingMetadata::isBookable() const {
    return m_bookable;
}
void OAIBettingMetadata::setBookable(const bool &bookable) {
    m_bookable = bookable;
    m_bookable_isSet = true;
}

bool OAIBettingMetadata::is_bookable_Set() const{
    return m_bookable_isSet;
}

bool OAIBettingMetadata::is_bookable_Valid() const{
    return m_bookable_isValid;
}

bool OAIBettingMetadata::isBooked() const {
    return m_booked;
}
void OAIBettingMetadata::setBooked(const bool &booked) {
    m_booked = booked;
    m_booked_isSet = true;
}

bool OAIBettingMetadata::is_booked_Set() const{
    return m_booked_isSet;
}

bool OAIBettingMetadata::is_booked_Valid() const{
    return m_booked_isValid;
}

bool OAIBettingMetadata::isLiveAvailable() const {
    return m_live_available;
}
void OAIBettingMetadata::setLiveAvailable(const bool &live_available) {
    m_live_available = live_available;
    m_live_available_isSet = true;
}

bool OAIBettingMetadata::is_live_available_Set() const{
    return m_live_available_isSet;
}

bool OAIBettingMetadata::is_live_available_Valid() const{
    return m_live_available_isValid;
}

bool OAIBettingMetadata::isMarketsCreated() const {
    return m_markets_created;
}
void OAIBettingMetadata::setMarketsCreated(const bool &markets_created) {
    m_markets_created = markets_created;
    m_markets_created_isSet = true;
}

bool OAIBettingMetadata::is_markets_created_Set() const{
    return m_markets_created_isSet;
}

bool OAIBettingMetadata::is_markets_created_Valid() const{
    return m_markets_created_isValid;
}

QDateTime OAIBettingMetadata::getMarketsUpdatedAt() const {
    return m_markets_updated_at;
}
void OAIBettingMetadata::setMarketsUpdatedAt(const QDateTime &markets_updated_at) {
    m_markets_updated_at = markets_updated_at;
    m_markets_updated_at_isSet = true;
}

bool OAIBettingMetadata::is_markets_updated_at_Set() const{
    return m_markets_updated_at_isSet;
}

bool OAIBettingMetadata::is_markets_updated_at_Valid() const{
    return m_markets_updated_at_isValid;
}

bool OAIBettingMetadata::isPandascoreReviewed() const {
    return m_pandascore_reviewed;
}
void OAIBettingMetadata::setPandascoreReviewed(const bool &pandascore_reviewed) {
    m_pandascore_reviewed = pandascore_reviewed;
    m_pandascore_reviewed_isSet = true;
}

bool OAIBettingMetadata::is_pandascore_reviewed_Set() const{
    return m_pandascore_reviewed_isSet;
}

bool OAIBettingMetadata::is_pandascore_reviewed_Valid() const{
    return m_pandascore_reviewed_isValid;
}

bool OAIBettingMetadata::isSettled() const {
    return m_settled;
}
void OAIBettingMetadata::setSettled(const bool &settled) {
    m_settled = settled;
    m_settled_isSet = true;
}

bool OAIBettingMetadata::is_settled_Set() const{
    return m_settled_isSet;
}

bool OAIBettingMetadata::is_settled_Valid() const{
    return m_settled_isValid;
}

bool OAIBettingMetadata::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_betting_group.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_blueprint.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_bookable_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_booked_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_live_available_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_markets_created_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_markets_updated_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_pandascore_reviewed_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_settled_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIBettingMetadata::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_betting_group_isValid && m_blueprint_isValid && m_bookable_isValid && m_booked_isValid && m_live_available_isValid && m_markets_created_isValid && m_markets_updated_at_isValid && m_pandascore_reviewed_isValid && m_settled_isValid && true;
}

} // namespace OpenAPI
