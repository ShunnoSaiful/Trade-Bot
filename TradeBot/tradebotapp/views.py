from django.shortcuts import render
from .models import Answer, Question, Plan, FeatureCategory, Description, Download, Section





def section_view(request):
	descriptions = Description.objects.all()
	section = Section.objects.all()
	answers = Answer.objects.all()
	plans = Plan.objects.all()
	questions = Question.objects.all()
	download = Download.objects.all()
	feature = FeatureCategory.objects.all()
	column = int(12/len(section))
	print(column)
	context = {
		"answers": answers,
		"questions": questions,
		"plans": plans,
		"descriptions": descriptions,
		"section": section,
		"download": download,
		"feature": feature,
		"column": column,
	}
	return render(request, "index.html", context)


