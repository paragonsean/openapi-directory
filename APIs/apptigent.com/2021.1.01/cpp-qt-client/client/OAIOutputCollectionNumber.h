/**
 * PowerTools Developer
 * Apptigent PowerTools Developer Edition is a powerful suite of API endpoints for custom applications running on any stack. Manipulate text, modify collections, format dates and times, convert currency, perform advanced mathematical calculations, shorten URL's, encode strings, convert text to speech, translate content into multiple languages, process images, and more. PowerTools is the ultimate developer toolkit.
 *
 * The version of the OpenAPI document: 2021.1.01
 * Contact: support@apptigent.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIOutputCollectionNumber.h
 *
 * 
 */

#ifndef OAIOutputCollectionNumber_H
#define OAIOutputCollectionNumber_H

#include <QJsonObject>

#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIOutputCollectionNumber : public OAIObject {
public:
    OAIOutputCollectionNumber();
    OAIOutputCollectionNumber(QString json);
    ~OAIOutputCollectionNumber() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    double getItem() const;
    void setItem(const double &item);
    bool is_item_Set() const;
    bool is_item_Valid() const;

    QList<double> getItems() const;
    void setItems(const QList<double> &items);
    bool is_items_Set() const;
    bool is_items_Valid() const;

    bool isStatus() const;
    void setStatus(const bool &status);
    bool is_status_Set() const;
    bool is_status_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    double m_item;
    bool m_item_isSet;
    bool m_item_isValid;

    QList<double> m_items;
    bool m_items_isSet;
    bool m_items_isValid;

    bool m_status;
    bool m_status_isSet;
    bool m_status_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIOutputCollectionNumber)

#endif // OAIOutputCollectionNumber_H
