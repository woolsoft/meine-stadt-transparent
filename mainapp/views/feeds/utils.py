from html import escape

from django.utils.translation import ugettext as _


def paper_description(paper):
    info = ''

    if paper.description:
        info += '<p>' + escape(paper.description) + '</escape>'

    info_bits = []
    if paper.paper_type:
        info_bits.append(paper.paper_type.paper_type)
    info_bits.append(paper.reference_number)
    info_bits.append(paper.legal_date.__str__())
    info += '<p>' + escape(', '.join(info_bits)) + '</p>'

    if paper.organizations.all():
        info += '<p>' + escape(_("Submitting Organizations")) + '</p><ul>'
        for orga in paper.organizations.all():
            info += '<li>' + escape(orga.name) + '</li>'
        info += '</ul>'

    if paper.persons.all():
        info += '<p>' + escape(_("Submitting Persons")) + '</p><ul>'
        for person in paper.persons.all():
            info += '<li>' + escape(person.name) + '</li>'
        info += '</ul>'

    if paper.main_file or paper.files.all():
        info += '<p>' + escape(_("Files")) + '</p><ul>'
        if paper.main_file:
            info += '<li><a href="' + escape(paper.main_file.get_default_link()) + '">'
            info += escape(paper.main_file.name) + '</a></li>'
        for file in paper.files.all():
            info += '<li><a href="' + escape(file.get_default_link()) + '">'
            info += escape(file.name) + '</a></li>'
        info += '</ul>'

    return info
