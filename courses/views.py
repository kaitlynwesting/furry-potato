from database.models.course import Course, Lesson
from django.views import generic


class CourseList(generic.ListView):
    model = Course
    template_name = 'courses/index.html'


class CourseDetails(generic.DetailView):
    model = Course
    template_name = 'courses/course_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lessons'] = context['object'].lessons.all()

        return context


class LessonDetails(generic.base.TemplateView):
    template_name = 'courses/lesson_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_course = Course.objects.get(slug=kwargs['course'])

        context['lesson'] = current_course.lessons.get(slug=kwargs['lesson'])
        context['course'] = current_course

        return context
