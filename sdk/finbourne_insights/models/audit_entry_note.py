# coding: utf-8

"""
    FINBOURNE Insights API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.735
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from finbourne_insights.configuration import Configuration


class AuditEntryNote(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'user_id': 'str',
        'text': 'str',
        'date': 'datetime'
    }

    attribute_map = {
        'user_id': 'userId',
        'text': 'text',
        'date': 'date'
    }

    required_map = {
        'user_id': 'required',
        'text': 'required',
        'date': 'required'
    }

    def __init__(self, user_id=None, text=None, date=None, local_vars_configuration=None):  # noqa: E501
        """AuditEntryNote - a model defined in OpenAPI"
        
        :param user_id:  (required)
        :type user_id: str
        :param text:  (required)
        :type text: str
        :param date:  (required)
        :type date: datetime

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._user_id = None
        self._text = None
        self._date = None
        self.discriminator = None

        self.user_id = user_id
        self.text = text
        self.date = date

    @property
    def user_id(self):
        """Gets the user_id of this AuditEntryNote.  # noqa: E501


        :return: The user_id of this AuditEntryNote.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this AuditEntryNote.


        :param user_id: The user_id of this AuditEntryNote.  # noqa: E501
        :type user_id: str
        """
        if self.local_vars_configuration.client_side_validation and user_id is None:  # noqa: E501
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                user_id is not None and len(user_id) < 1):
            raise ValueError("Invalid value for `user_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._user_id = user_id

    @property
    def text(self):
        """Gets the text of this AuditEntryNote.  # noqa: E501


        :return: The text of this AuditEntryNote.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this AuditEntryNote.


        :param text: The text of this AuditEntryNote.  # noqa: E501
        :type text: str
        """
        if self.local_vars_configuration.client_side_validation and text is None:  # noqa: E501
            raise ValueError("Invalid value for `text`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                text is not None and len(text) < 1):
            raise ValueError("Invalid value for `text`, length must be greater than or equal to `1`")  # noqa: E501

        self._text = text

    @property
    def date(self):
        """Gets the date of this AuditEntryNote.  # noqa: E501


        :return: The date of this AuditEntryNote.  # noqa: E501
        :rtype: datetime
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this AuditEntryNote.


        :param date: The date of this AuditEntryNote.  # noqa: E501
        :type date: datetime
        """
        if self.local_vars_configuration.client_side_validation and date is None:  # noqa: E501
            raise ValueError("Invalid value for `date`, must not be `None`")  # noqa: E501

        self._date = date

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AuditEntryNote):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AuditEntryNote):
            return True

        return self.to_dict() != other.to_dict()
